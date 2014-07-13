import sys
import os
sys.path.append('../')
sys.path.append('/home/billy/programs/Sublime Text 2/')
sys.path.append('/home/billy/.config/sublime-text-2/Packages/')
import re
import unittest
import json
from pprint import pprint
# import sublime

#from mxunit_plugin import MxunitCommand



class MXUnitTest(unittest.TestCase):
	
	def test_read_json_data(self):
		fn = os.path.join(os.path.dirname(__file__), 'test_results_fixture.json')
		test_results_raw=open(fn)
		tests = json.load( test_results_raw )
		# pprint(tests)
		passes = len( [ test for test in tests if test['TESTSTATUS']=='Passed'] )
		self.assertEquals( 33, passes )
		
	
	def test_read_json_show_failures_only(self):
		test_results_raw=open('test_results_fixture.json')
		tests = json.load( test_results_raw )
		# pprint(tests)
		failed =  [ test for test in tests if test['TESTSTATUS']=='Failed' ] 
		for item in failed:
			pass #pprint (item)
		self.assertEquals( 2, len(failed) )


	#To Do: Hanlde cffunction name="asdasd" . HTML attribute
	def test_parse_line_for_test_method_name(self):
		line = 'function thisIs_thE_test-MEt0D_nam3(asd,asd,asd)'
		lines= ['	pattern = re.compile("""', 
				'function thisIs_thE_test-MEt0D_nam3(asd,asd,asd)',
				'function __filterTestForStruct(){',
				'	<cffunction name="thisIs_thE_test-MEt0D_in_CFFUNCTION"',
				'<cffunction    name =  "thisIs_thE_test-MEt0D_in_CFFUNCTION"']
		# cmd = MxunitCommand()
		for line in lines:
			actual = parse_line(line)
			# actual = self.parse_line(line)
			print actual
			# return
			expected = 'thisIs_thE_test-MEt0D_nam3'
			# self.assertEquals( expected,actual )


def parse_line(line):
	"""
	From a line of text gets the function name (Only with script. Not tags, yet)
	"""
	pattern = re.compile("""
		[ \t]*
		(private|package|remote|public)*[ ]*
		(any|string|array|numeric|boolean|component|struct|void)*[ ]*
		(function[ ]+|\<cffunction[ ]+name[ ]*=[ ]*\"?)([_\-a-z][a-z0-9_\-]+)
		""", 
		re.VERBOSE|re.MULTILINE|re.IGNORECASE)
	m = pattern.match(line)
	#return the 5th gouped regex, which should be the function name
	ret_val =  m.group(4) if m else ''
	return ret_val