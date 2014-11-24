# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import HTML

# <markdowncell>

# ### HTML
# JSinput offers perhaps the most intriguing problem type in the edX system; endless freedom to adapt javascript visualizations for graded assessment. However, it consists of one of the most challenging assessment creation workflows in edX. JSinput problems involve HTML, Javascript, and CSS, all graded within a custom response Python script. 
# 
# _Discuss studio workflow_: HTML/JS edited outside the system. Once integrated, all python grading takes place within a rudimentary modal window.
# 
# #### Insert image for JSinput workflow via studio
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
        
        <div style="width: 100%; overflow: hidden;">
            <div id='jxgbox1' class='jxgbox' style='width:350px; height:350px; float:left; border: solid #1f628d 2px;'></div>
        </div>
        
        <input class="btn" type="button" value="Console Log State" onClick="logState()">
        <input class="btn" type="button" value="Pass State" onClick="passState()">
        
        <div id="spaceBelow">State:</div>

        
        <script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>
        <script type='text/javascript'>

            bboxlimits = [-1.1, 12, 12, -1.1];
            //var board1 = JXG.JSXGraph.initBoard('jxgbox1', {boundingbox: bboxlimits, axis: {withlabel: true, name: "Price"}});
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

            //var f1 = board.create('functiongraph', [function(x){ return  Math.pow(x,1.0)},0.1,15], {strokeColor:'gray',strokeWidth:'1',dash:'1'});
            //var f1 = board.create('functiongraph', [function(x){ return  Math.pow(x,1.0)},0.1,15], {strokeColor:'black',strokeWidth:'3',name:'AD'});

            var p1 = board.create('point',[-2.0,-2.0],{withLabel:false});
            var p2 = board.create('point',[12.0,12.0],{withLabel:false});
            var line1 = board.create('line',[p1,p2],{strokeColor:'black',strokeWidth:'3',name:'AD',withLabel:false});
            var line2 = board.create('line',[[0.0,0.0],[12.0,12.0]],{strokeColor:'gray',strokeWidth:'1',dash:'1',fixed:true});


            var f2 = board.create('functiongraph', [function(x){ return Math.abs(10.0/x);},0.01,15], {strokeColor:'black',strokeWidth:'3',name:'SRAS'});

            //var glider1 = board1.create('glider', [2.0, 1.5, g]);
            //var i = board.create('intersection', [line1, f2, 0], {withLabel:false,strokeColor:'blue'});

            var kernel = IPython.notebook.kernel;
            
            //console.log(state);
            //kernel.execute(state);

            logState = function() {
                var state = {'y1':line1.point1.Y(),'y2':line1.point2.Y()};
                statestr = JSON.stringify(state);
                console.log(state);
                return statestr
            }
            
            passState = function(){
                var state = {'y1':line1.point1.Y(),'y2':line1.point2.Y()};
                statestr = JSON.stringify(state);
                //document.write(statestr);
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

import json
ans = json.loads(state)

class curveGrader:

# <codecell>


