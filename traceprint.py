import json
import os

#Transform
def union( *args ):
	ret = []
	for a in args:
		ret.append( a )
	return { "type": "union", "children": ret }

def difference( a, b ):
	return { "type": "difference", "children": [a, b] }
	
def intersection( *args ):
	ret = []
	for a in args:
		ret.append( a )
	return { "type": "intersection", "children": ret }

def translate( x, y=None, z=None ):
	def func( *args ):
		if y is not None:
			vec = [float(x), float(y), float(z)]
		else:
			vec = [float(x[0]), float(x[1]), float(x[2])]
		return { "type": "translate", "x": vec[0], "y": vec[1], "z": vec[2], "children": union( *args ) }
	return func

#Primitives
def box( x, y, z ):
	return { 
		"type": "box", 
		"x": float(x), 
		"y": float(y), 
		"z": float(z)
	}

def sphere( r, slices=16, stacks=8 ):
	return { "type": "sphere", "r": float(r), "slices": int(slices), "stacks": int(stacks) }

def cylinder( r, height, slices=8 ):
	return { "type": "cylinder", "r": float(r), "height": float(height), "slices": int(slices) }
	
def stl( filepath, abspath=True ):
	return { "type": "stl", "path": os.path.abspath( filepath ) if abspath else filepath }

def polyhedron( points, faces ):
	return { "type": "polyhedron", "points": points, "faces": faces }
	
#Modifiers
def color( r, g, b ):
	def func( *args ):
		return { "type": "color", "r": float(r), "g": float(g), "b": float(b), "children": union( *args ) }
	return func

def module( name ):
	return { "type": "module", "name": name }
	
#Helpers	
def write_out( filename, object ):
	if "main" in object:
		out = { "geometry": object }
	else:
		out = { "geometry": { "main": object } }
	with open( filename, "w" ) as f:
		f.write( json.dumps( out, indent=3 ) )

def from_solid( obj ):
	pass