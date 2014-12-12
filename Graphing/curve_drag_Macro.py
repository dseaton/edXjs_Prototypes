# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import HTML

# <markdowncell>

# #Macroeconmics - general feature for dragging curves

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


