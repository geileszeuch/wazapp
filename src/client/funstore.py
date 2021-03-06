'''
Copyright (c) 2012, Tarek Galal <tarek@wazapp.im>

This file is part of Wazapp, an IM application for Meego Harmattan platform that
allows communication with Whatsapp users

Wazapp is free software: you can redistribute it and/or modify it under the 
terms of the GNU General Public License as published by the Free Software 
Foundation, either version 2 of the License, or (at your option) any later 
version.

Wazapp is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
Wazapp. If not, see http://www.gnu.org/licenses/.
'''
class FunStore():
	
	def __init__(self):
		self.container = {}

	def clear(self):
		self.container = {}
	
	def get(self,paramKey):
		try:
			return self.container[paramKey.toString()];
		except KeyError:
			return None

	def put(self,paramKey,paramFMessage):
		self.container[paramKey.toString()] = paramFMessage;

	def elements(self):
		return self.container
	
	def remove(self,paramKey):
		self.container.pop(paramKey.toString());
