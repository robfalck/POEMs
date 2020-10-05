POEM ID: 035  
Title: More generalized behavior in promoted inputs.  
authors: [robfalck]  
Competing POEMs: N/A  
Related POEMs: N/A  
Associated implementation PR:

##  Status

- [x] Active
- [ ] Requesting decision
- [ ] Accepted
- [ ] Rejected
- [ ] Integrated


## Motivation

The current input promotion system has exposed an inconsistency that can cause confusion among users and makes certain connections impossible.

## Description

Currently, if a variable is promoted using src_indices and it receives no connection, an automatic IndepVarComp output is created for it using those source indices to infer its shape.

If an output is connected to the promoted input variable, using the `connect` method, then the src_indices are applied as specified in the promote. 
It is possible that a promoted input has src_indices specified, but src_indices are also specified in the connect statement. 
If the src_indices are identical in both cases, then there is no problem. 
If they are not the same, as of V3.4.0, you always get an error. 

There is a particular case, involving the broadcasting/duplicating of lower dimensional outputs to higher dimensional inputs, where OpenMDAO should allow the discrepency and process it correctly. 
This specific case is when src_indices are used to broadcast some values from a low dimensional output to a higher dimensional input. 

### Examples
Consider an output (x) of size 1, and an input (y) of size 4: 
`group.connect('x','y', src_indices=[0,0,0,0])` broadcasts the scalar output to a length 4 input with the value of `x` copied 4 times. 

Consider an output (x) of size 2, and an input (y) of size 4: 
`group.connect('x','y', src_indices=[0,1,0,1])` broadcasts the length 2 output to an input that has two copies concatenated together. 


These examples currently work as of OpenMDAO V3.4.0, however you can mix `promote` and  `connect` opertaions in a way that is sensible, but currently doesn't work. 

Consider an output ('c0.x') of size 4, and in input 'c1.y' of size 6. 
From the perspective of the promoted input, `y`, a length 2 vector is expected which then gets broadcast out to make 3 copies of it. 
From the perspective of the connection from the output, you want to grab the middle two entries of the array to be the source of that broadcast.

That would look something like this. 
```
group.promotes('c1', inputs=['y'], src_indices=[0,1,0,1,0,1])
group.connect('c0.x', 'y', src_indices=[2,3])
```

The intention is fairly clear. A mapping needs to happen to translate [0,1,0,1,0,1] to [2,3,2,3,2,3,].  
As of V3.4.0 this causes an error, because there is some potential ambiguity here due to the mismatch in size between the source and target sides of the connection. 
Did the user intend for a mapping to occur or was there a mistake? Impossible to tell. 
This POEM seeks to allow such mappings by compatible extension of the `promotes` api to remove the ambiguity. 

## Proposed new API


1. `src_shape` is added as an argument to `promotes` which specifies the apparent shape of the promoted input (if connecting to it) or the related AutoIVC output (if left unconnected).

2. If `src_shape` is specified, then `src_indices` are computed relative to the given shape and a mapping will occur for any connected value, as long as the shapes match the `src_shape` value. 

3. If `src_shape` is not given, OpenMDAO will continue to function the same way it has. Any ambiguity in meaning from conflicting src indices will raise an error. 

4. `src_shape` also becomes an argument to `set_input_defaults` to force a common shape in the input or auto_ivc output

## Backwards Incompatible API Change

`src_indices` becomes a deprecated argument in `add_input`.  
Since it only comes into play relative to promotion or connection, 
specifying it in `add_input` is logically inconsistent. 

This is a fairly minor change, but given how long the existing API's have been in existence it warrants a fairly long deprecation period. 
Existing models will continue to work, with the deprecation warning, till OpenMDAO 4.0
