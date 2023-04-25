'use strict';var features={};import{AssertionError,AttributeError,BaseException,DeprecationWarning,Exception,IndexError,IterableError,KeyError,NotImplementedError,RuntimeWarning,StopIteration,UserWarning,ValueError,Warning,__JsIterator__,__PyIterator__,__Terminal__,__add__,__and__,__call__,__class__,__envir__,__eq__,__floordiv__,__ge__,__get__,__getcm__,__getitem__,__getslice__,__getsm__,__gt__,__i__,__iadd__,__iand__,__idiv__,__ijsmod__,__ilshift__,__imatmul__,__imod__,__imul__,__in__,__init__,__ior__,
__ipow__,__irshift__,__isub__,__ixor__,__jsUsePyNext__,__jsmod__,__k__,__kwargtrans__,__le__,__lshift__,__lt__,__matmul__,__mergefields__,__mergekwargtrans__,__mod__,__mul__,__ne__,__neg__,__nest__,__or__,__pow__,__pragma__,__pyUseJsNext__,__rshift__,__setitem__,__setproperty__,__setslice__,__sort__,__specialattrib__,__sub__,__super__,__t__,__terminal__,__truediv__,__withblock__,__xor__,abs,all,any,assert,bool,bytearray,bytes,callable,chr,copy,deepcopy,delattr,dict,dir,divmod,enumerate,filter,float,
getattr,hasattr,input,int,isinstance,issubclass,len,list,map,max,min,object,ord,pow,print,property,py_TypeError,py_iter,py_metatype,py_next,py_reversed,py_typeof,range,repr,round,set,setattr,sorted,str,sum,tuple,zip}from"./org.transcrypt.__runtime__.js";import*as __module_features__ from"./features.js";__nest__(features,"",__module_features__);var __name__="formula.pg_formula_requirement";export var Requirement_Mode=__class__("Requirement_Mode",[object],{__module__:__name__,NONE:0,ANY:1,ALL:2});export var RM=
Requirement_Mode;export var Formula_Requirement=__class__("Formula_Requirement",[object],{__module__:__name__,get __init__(){return __get__(this,function(self){var req_mode=RM.ALL;if(arguments.length){var __ilastarg0__=arguments.length-1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=__allkwargs0__[__attrib0__];break;case "req_mode":var req_mode=
__allkwargs0__[__attrib0__];break}}var reqs=tuple([].slice.apply(arguments).slice(1,__ilastarg0__+1))}else var reqs=tuple();self.req_mode=req_mode;self.reqs=reqs})},get met(){return __get__(this,function(self){if(arguments.length){var __ilastarg0__=arguments.length-1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=__allkwargs0__[__attrib0__];
break}}}else;var req_checkers=dict([[RM.NONE,features.none],[RM.ANY,features.any],[RM.ALL,features.all]]);return req_checkers[self.req_mode](...self.reqs)})}});export var FR=Formula_Requirement;

//# sourceMappingURL=formula.pg_formula_requirement.map