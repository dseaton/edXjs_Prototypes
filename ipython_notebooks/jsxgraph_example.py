# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import HTML

# <markdowncell>

# ### HTML
# JSinput offers perhaps the most intriguing assessment type available in the edX system; the endless creative freedom of javascript visualizations combined with graded assessment. However, JSinput consists of one of the most challenging assessment creation workflows in edX. Graded assessment involve HTML, Javascript, and CSS, all of which leads to a JSON "state" passed to a custom response grading script written in Python. 
# 
# iPython notebooks provide a sensible approach to stream lining the JSinput workflow. They provide an HTML/JS/CSS interface with the luxury of python interactions. HTML/JS/CSS is written within an HTML cell, from which, the associated "state" of a given interactive can be passed to Python - the native language of an iPython notebook.
# 
# _Discuss studio workflow_: HTML/JS edited outside the system. Once integrated, all python grading takes place within a rudimentary modal window.
# 
# #### Insert image for JSinput workflow via studio
# 
# #### Insert image for iPython notebook workflow and incorporation with Studio
# 
# ### Hopes for the future
# The iPython workflow is a small step toward improving the current JSinput workflow. Our hope is that these examples will inspire dialogue on improving the interface, as well as providing broader training to instructors and course teams that lack a background in HTML, CSS, Javascript, and Python.
#  

# <markdowncell>

# #Simple HTML example
# Below is a simple example of writing HTML within an iPython Notebook. Three key features:
# 
# * %%HTML - the '%%' signal [_cell magic_](http://ipython.org/ipython-doc/2/interactive/reference.html#magic-command-system), which in this case, registers all cell input as HTML.
# * See "style" blocks - this is where we add some rudimentary CSS styling. Go ahead, try adjusting the font size seen in the output below the cell.
# * See "body" blocks - this is where we write HTML to be displayed. It will also be where our Javascript lives in most examples.

# <codecell>

%%html
<!DOCTYPE html>
<html>
    <head>
        <style>
            test {
                font-size: 250%;
                color: Orange;
            }
        </style>
    </head>
    <body>
        <test>Hey you - world!</test>
    </body>
</html>

# <markdowncell>

# #Interactive Graphs using JSXgraph
# Now we jump into an interactive graphing example. You can read more about JSXgraph [here](http://ipython.org/ipython-doc/2/interactive/reference.html#magic-command-system).
# 
# 

# <codecell>

%%html

<!DOCTYPE html>
<html>
    <head>
        <style> 
            body {
                margin: 10px;
                /*padding-top: 40px;*/
            }
        </style>
    </head>

    <body>
        <!-- COMMENT: Define the jxgbox - aka, where all the interactive graphing will go. -->
        <div style="width: 100%; overflow: hidden;">
            <div id='jxgbox1' class='jxgbox' style='width:350px; height:350px; float:left; border: solid #1f628d 2px;'></div>
        </div>
        
        <!-- COMMENT: Buttons below are used to add debugging features to an interactive. Conole logging allows you to see
            output within a browser's console. Try reading about Chrome's console. -->
        
        <input class="btn" type="button" value="Pass State for Grading" onClick="passState()">
        <div id="spaceBelow">State:</div>

        
        <!-- COMMENT: Where our Javascript begins. -->
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>
        <script type='text/javascript'>

            bboxlimits = [-1.1, 12, 12, -1.1];
            var board = JXG.JSXGraph.initBoard('jxgbox1', {axis:false, 
                                                    showCopyright: false,
                                                    showNavigation: false,
                                                    zoom: false,
                                                    pan: false,
                                                    boundingbox:bboxlimits,
                                                    grid: true
            });
            
            xaxis = board.create('axis', [[0, 0], [12, 0]], {withLabel: true, name: "Real GDP", label: {offset: [320,-20]}});
            yaxis = board.create('axis', [[0, 0], [0, 12]], {withLabel: true, name: "Price Level", label: {offset: [-60,260]}});

            var c1 = [0.0,0.0];
            var c2 = [12.0,12.0];
            var line1 = board.create('line',[c1,c2],{strokeColor:'gray',strokeWidth:'2',dash:'1',fixed:true});
            var line2 = board.create('line',[c1,c2],{strokeColor:'black',strokeWidth:'3',name:'AD',withLabel:false});

            var f1 = board.create('functiongraph', [function(x){ return Math.abs(10.0/x);},0.01,15], {strokeColor:'black',strokeWidth:'3',name:'SRAS'});

            var kernel = IPython.notebook.kernel;
            
            passState = function(){
                console.log(line2);
                var state = {'line1':{'p1':[line1.point1.X(),line1.point1.Y()],'p2':[line1.point2.X(),line1.point2.Y()]},
                             'line2':{'p1':[line2.point1.X(),line2.point1.Y()],'p2':[line2.point2.X(),line2.point2.Y()]}
                             };
                statestr = JSON.stringify(state);
                document.getElementById('spaceBelow').innerHTML += '<br>'+statestr;
                var command = "state = '" + statestr + "'";
                console.log(command);

                var kernel = IPython.notebook.kernel;
                kernel.execute(command);

                return statestr
            }
            
            function set_value(){
                var var_value = state;
                console.log(var_value);
                var command = "state = '" + var_value + "'";
                console.log("Executing Command: " + command);

                var kernel = IPython.notebook.kernel;
                kernel.execute(command);
            }
            
        </script>
    </body>
</html>

# <codecell>

def overallGrader(e, ans):
    return {'ok': True, 'msg': 'Good job!'}

import json
answer = json.loads(state)

class gradeCurves:
    def __init__(self):
        return None

    def diff1DPoints(self,p2,p1):
#         print point2 - point1
        return p2 - p1

### Not scalable, but I write this out so it is transparent
# Curve 1: x and y coords
c1x1 = answer['line1']['p1'][0]
c1x2 = answer['line1']['p2'][0]
c1y1 = answer['line1']['p1'][1]
c1y2 = answer['line1']['p2'][1]
# Curve 2: x and y coords
c2x1 = answer['line2']['p1'][0]
c2x2 = answer['line2']['p2'][0]
c2y1 = answer['line2']['p1'][1]
c2y2 = answer['line2']['p2'][1]
    
if (gradeCurves().diff1DPoints(c2x1,c1x1) < -0.5 and 
    gradeCurves().diff1DPoints(c2x2,c1x2) < -0.5 and
    gradeCurves().diff1DPoints(c2y1,c1y1) > 0.5 and
    gradeCurves().diff1DPoints(c2y2,c1y2) > 0.5):
    print {'ok': True, 'msg': 'Good job.'}
else:
    print {'ok': False, 'msg': 'Something wrong.'}

# <codecell>


