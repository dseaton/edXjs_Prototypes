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

%%HTML

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
            <div id='jxgbox1' class='jxgbox' style='width:450px; height:350px; float:left; border: solid #1f628d 2px;'></div>
        </div>
        
        <!-- COMMENT: Buttons below are used to add debugging features to an interactive. Conole logging allows you to see
            output within a browser's console. Try reading about Chrome's console. -->
        
        <input class="btn" type="button" value="Pass State for Grading" onClick="getInput()">
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
                                                    grid: false,
                                                    hasMouseUp: true, 
            });
            
            xaxis = board.create('axis', [[0, 0], [12, 0]], {withLabel: true, name: "Real GDP", label: {offset: [320,-20]}});
            yaxis = board.create('axis', [[0, 0], [0, 12]], {withLabel: true, name: "Price Level", label: {offset: [-60,260]}});

            //Axes
            xaxis.removeAllTicks();
            yaxis.removeAllTicks();
            var xlabel = board.create('text',[-1,10,"Price<br>Level"],{fixed:true});
            var ylabel = board.create('text',[9,-0.5,"Real GDP"],{fixed:true});
            
            //Define Functions
            c1 = [-2.0,-2.0]
            c2 = [12.0,12.0]
            var p1 = board.create('point',[-2.0,-2.0],{withLabel:false,visible:false});
            var p2 = board.create('point',[12.0,12.0],{withLabel:false,visible:false});
            var dragLine = board.create('line',[p1,p2],{strokeColor:'blue',strokeWidth:'3',name:'AD',withLabel:false});
            var staticLine = board.create('line',[c1,c2],{strokeColor:'gray',strokeWidth:'1',dash:'1',fixed:true});
            
            var f2 = board.create('functiongraph', [function(x){ return Math.abs(10.0/x);},0.01,15], {strokeColor:'black',strokeWidth:'3',name:'SRAS'});
            
            //Standard edX JSinput functions
            getInput = function(){
                state = {"dragLine":{'p1Y':dragLine.point1.Y(),'p2Y':dragLine.point2.Y()},
                         "staticLine":{'p1Y':staticLine.point1.Y(),'p2Y':staticLine.point2.Y()}};
                statestr = JSON.stringify(state);
                console.log(statestr)
                
                //IPython Notebook Considerations
                document.getElementById('spaceBelow').innerHTML += '<br>'+statestr;
                var command = "state = '" + statestr + "'";
                console.log(command);

                //Kernel
                var kernel = IPython.notebook.kernel;
                kernel.execute(command);

                return JSON.stringify(statestr);
            }

            getState = function(){
                state = {input: JSON.parse(getInput())};
                statestr = JSON.stringify(state);
                // $('#msg').html('getstate ' + statestr);
                return statestr
            }

            setState = function(statestr){
                console.log(statestr);
                // alert(statestr);
                initializeVector(statestr);
                $('#msg').html('setstate ' + statestr);
                state = JSON.parse(statestr);
                console.log(state);
                initializeVector(state);
                console.debug('State updated successfully from saved.');
            }
            
        </script>
    </body>
</html>

# <markdowncell>

# ### State is now in the Kernel
# So you can begin using python to create your custom grader. Below is a simple example checking that the y-coordinates of the blue-draggable line are above the original placement (i.e., the curve has been shifted up).

# <codecell>

import json
answer = json.loads(state)

def dist1D(xf,xi):
    print xf,xi,xf-xi
    return xf-xi
    
delta = dist1D(answer['dragLine']['p1Y'],answer['staticLine']['p1Y'])
if delta > 0:
    if delta > 0.5:
        print {'ok': True, 'msg': 'Good job.'}
elif delta < 0:
    print {'ok': False, 'msg': 'Please rethink your solution - explanation.'}
else:
    print {'ok': False, 'msg': 'Something wrong.'}

# <codecell>


