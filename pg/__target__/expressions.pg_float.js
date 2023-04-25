'use strict';import{AssertionError,AttributeError,BaseException,DeprecationWarning,Exception,IndexError,IterableError,KeyError,NotImplementedError,RuntimeWarning,StopIteration,UserWarning,ValueError,Warning,__JsIterator__,__PyIterator__,__Terminal__,__add__,__and__,__call__,__class__,__envir__,__eq__,__floordiv__,__ge__,__get__,__getcm__,__getitem__,__getslice__,__getsm__,__gt__,__i__,__iadd__,__iand__,__idiv__,__ijsmod__,__ilshift__,__imatmul__,__imod__,__imul__,__in__,__init__,__ior__,__ipow__,
__irshift__,__isub__,__ixor__,__jsUsePyNext__,__jsmod__,__k__,__kwargtrans__,__le__,__lshift__,__lt__,__matmul__,__mergefields__,__mergekwargtrans__,__mod__,__mul__,__ne__,__neg__,__nest__,__or__,__pow__,__pragma__,__pyUseJsNext__,__rshift__,__setitem__,__setproperty__,__setslice__,__sort__,__specialattrib__,__sub__,__super__,__t__,__terminal__,__truediv__,__withblock__,__xor__,abs,all,any,assert,bool,bytearray,bytes,callable,chr,copy,deepcopy,delattr,dict,dir,divmod,enumerate,filter,float,getattr,
hasattr,input,int,isinstance,issubclass,len,list,map,max,min,object,ord,pow,print,property,py_TypeError,py_iter,py_metatype,py_next,py_reversed,py_typeof,range,repr,round,set,setattr,sorted,str,sum,tuple,zip}from"./org.transcrypt.__runtime__.js";import{Mixin_Renderable_Operation}from"./mixins.pg_mixin_renderable_operation.js";import{Mixin_Renderable}from"./mixins.pg_mixin_renderable.js";import{Mixin_Generatable}from"./mixins.pg_mixin_generatable.js";import{FR}from"./formula.pg_formula_requirement.js";
import{FP}from"./formula.pg_formula_pattern.js";import{FN}from"./formula.pg_formula_node.js";import{Variable}from"./expressions.pg_variable.js";import*as PG_N from"./expressions.pg_number.js";import{Function_Call,RT}from"./expressions.pg_function_call.js";import{JS_Random as R}from"./util.js_random.js";var __name__="expressions.pg_float";export var Float=__class__("Float",[Mixin_Generatable,Mixin_Renderable],{__module__:__name__,get get_patterns(){return __get__(this,function(self){if(arguments.length){var __ilastarg0__=
arguments.length-1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=__allkwargs0__[__attrib0__];break}}}else;return[FP(FN(Float_Literal),__kwargtrans__({weight:4})),FP(FN(Float_Operation),__kwargtrans__({weight:1})),FP(FN(Function_Call,__kwargtrans__({args:[RT.FLOAT]})),__kwargtrans__({weight:1,reqs:FR("functions")})),FP(FN(Variable,"float"),
__kwargtrans__({weight:2,reqs:FR("variables")}))]})}});export var Float_Operation=__class__("Float_Operation",[Mixin_Generatable,Mixin_Renderable_Operation],{__module__:__name__,get get_patterns(){return __get__(this,function(self){if(arguments.length){var __ilastarg0__=arguments.length-1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=
__allkwargs0__[__attrib0__];break}}}else;return[FP(FN(PG_N.Number),"+",FN(Float),__kwargtrans__({weight:3})),FP(FN(Float),"+",FN(PG_N.Number),__kwargtrans__({weight:3})),FP(FN(PG_N.Number),"-",FN(Float),__kwargtrans__({weight:3})),FP(FN(Float),"-",FN(PG_N.Number),__kwargtrans__({weight:3})),FP(FN(PG_N.Number),"*",FN(Float),__kwargtrans__({weight:2})),FP(FN(Float),"*",FN(PG_N.Number),__kwargtrans__({weight:2})),FP(FN(PG_N.Number),"/",FN(PG_N.Number),__kwargtrans__({weight:2})),FP(FN(PG_N.Number),"//",
FN(Float),__kwargtrans__({weight:2})),FP(FN(Float),"//",FN(PG_N.Number),__kwargtrans__({weight:2})),FP(FN(PG_N.Number),"**",FN(Float)),FP(FN(Float),"**",FN(PG_N.Number))]})}});export var Float_Literal=__class__("Float_Literal",[Mixin_Generatable,Mixin_Renderable],{__module__:__name__,get __init__(){return __get__(this,function(self,lower,upper){if(typeof lower=="undefined"||lower!=null&&lower.hasOwnProperty("__kwargtrans__"))var lower=-50;if(typeof upper=="undefined"||upper!=null&&upper.hasOwnProperty("__kwargtrans__"))var upper=
100;if(arguments.length){var __ilastarg0__=arguments.length-1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=__allkwargs0__[__attrib0__];break;case "lower":var lower=__allkwargs0__[__attrib0__];break;case "upper":var upper=__allkwargs0__[__attrib0__];break}}}else;__super__(Float_Literal,"__init__")(self);self.lower=lower;self.upper=upper})},
get generate(){return __get__(this,function(self){if(arguments.length){var __ilastarg0__=arguments.length-1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=__allkwargs0__[__attrib0__];break}}}else;return R.number_between(self.lower,self.upper,true)})}});

//# sourceMappingURL=expressions.pg_float.map