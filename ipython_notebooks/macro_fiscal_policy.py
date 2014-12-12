# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import HTML

# <markdowncell>

# #Macroeconmics - Fiscal Policy
# Taking some themes from the following [youtube video](https://www.youtube.com/watch?v=v4dmUrUqvWs).
# 
# Potential Question: "If taxes are increased, which curve represents the new aggregate demand (AD)?

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
        
        
        <!--START-BUTTON FOR PASS STATE-->
        <!-- COMMENT: Buttons below are used to add debugging features to an interactive. Conole logging allows you to see
            output within a browser's console. Try reading about Chrome's console. -->
        
        <input class="btn" type="button" value="Pass State for Grading" onClick="passState()">
        <div id="spaceBelow">State:</div>
        <!--END-BUTTON FOR PASS STATE-->
        
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
            var f1 = board.create('functiongraph', [function(x){ return 10.0/x;},0.01,15], {strokeColor:'DarkGrey',strokeWidth:'3',name:'AD1'});
            var f1label = board.create('text',[3.5,6,"AD#1"]);
            var f2 = board.create('functiongraph', [function(x){ return 10.0/(x-1.0)+1.0;},0.01,15], {strokeColor:'DarkGrey',strokeWidth:'3',name:'AD2'});
            var f2label = board.create('text',[1.0,4.5,"AD#2"]);
            var f3 = board.create('functiongraph', [function(x){ return Math.exp(0.3*x);},0.01,15], {strokeColor:'black',strokeWidth:'3',name:'SRAS',highlight:false});

            //First set of dashed lines
            var i13 = board.create('intersection', [f1, f3, 0], {visible:false});
            var d1 = board.create('line',[[i13.X(), 0],[i13.X(),i13.Y()]],{straightFirst:false, straightLast:false,
                                                                           strokeColor:'gray',strokeWidth:'2',
                                                                           dash:'1',fixed:true}
                                  );
            var d2 = board.create('line',[[0, i13.Y()],[i13.X(),i13.Y()]],{straightFirst:false, straightLast:false,
                                                                           strokeColor:'gray',strokeWidth:'2',
                                                                           dash:'1',fixed:true}
                                  );
            
            //Second set of dashed lines
            var i23 = board.create('intersection', [f2, f3, 0], {visible:false});
            var d3 = board.create('line',[[i23.X(), 0],[i23.X(),i23.Y()]],{straightFirst:false, straightLast:false,
                                                                           strokeColor:'gray',strokeWidth:'2',
                                                                           dash:'1',fixed:true}
                                  );
            var d4 = board.create('line',[[0, i23.Y()],[i23.X(),i23.Y()]],{straightFirst:false, straightLast:false,
                                                                           strokeColor:'gray',strokeWidth:'2',
                                                                           dash:'1',fixed:true}
                                  );
        
            var kernel = IPython.notebook.kernel;
            
            f1.on('down', function () {
                resetColors(f1);
                resetColors(f2);
                f1.setAttribute({strokeColor: 'red',strokeWidth: 4});
            });
            
            f2.on('down', function () {
                resetColors(f1);
                resetColors(f2);
                f2.setAttribute({strokeColor: 'red',strokeWidth: 4});
            });
            
            resetColors = function(curve) {
                curve.setAttribute({strokeColor: 'DarkGrey',strokeWidth: 3});
            }
            
            
            //Grading Functions
            
            //START-PASS STATE TO IPYTHON KERNEL
            passState = function(){
                var state = {'f1':f1.getAttribute('strokeColor'),'f2':f2. getAttribute('strokeColor')};
                statestr = JSON.stringify(state);
                document.getElementById('spaceBelow').innerHTML += '<br>'+statestr;
                var command = "state = '" + statestr + "'";
                console.log(command);

                var kernel = IPython.notebook.kernel;
                kernel.execute(command);

                return statestr
            }
                
            //END-PASS STATE TO IPYTHON KERNEL
            
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

# <markdowncell>

# ### Save HTML file
# Removes any IPython Notebook specific functions

# <codecell>

# def findHTMLInputCell(**kwargs):
#     specify

tmpfile = _i88
tmpfile = re.sub('%%HTML','',tmpfile)
tmpfile = re.sub(r'<!--START-BUTTON FOR PASS STATE(.*?)END-BUTTON FOR PASS STATE-->','',tmpfile,flags=re.DOTALL)
tmpfile = re.sub(r'//START-PASS STATE TO IPYTHON KERNEL(.*?)//END-PASS STATE TO IPYTHON KERNEL','',tmpfile,flags=re.DOTALL)
with open('macro_fiscal_policy.html','w') as hfile:
    hfile.write(tmpfile)
print tmpfile

# <codecell>

def overallGrader(e, ans):
    return {'ok': True, 'msg': 'Good job!'}

import json
answer = json.loads(state)
    
if answer['f1'] == 'red' and answer['f2'] == 'DarkGrey':
    print {'ok': True, 'msg': 'Good job.'}
else:
    print {'ok': False, 'msg': 'Something wrong.'}

# <codecell>

'''
<problem display_name="webGLDemo">
<script type="loncapa/python">
<![CDATA[
import json

def dist1D(xf,xi):
    #print xf,xi,xf-xi
    return xf-xi

def vglcfn(e, ans):
    answer = json.loads(json.loads(ans)['answer'])
    #return {'ok': False, 'msg': '%s' % str(answer)}

    delta = dist1D(answer['dragLine']['p1Y'],answer['staticLine']['p1Y'])
    if delta < 0:
        if abs(delta) > 0.5:
            return {'ok': True, 'msg': 'Good job.'}
    elif delta < 0:
        return {'ok': False, 'msg': 'Please rethink your solution - explanation.'}
    else:
        return {'ok': False, 'msg': 'Something wrong.'}

]]>
</script>
  
<p>
Text of the question goes here. Feel free to make it fancier.
</p>
  
<customresponse cfn="vglcfn">
  <jsinput gradefn="getInput"
    get_statefn="getState"
    set_statefn="setState"
    initial_state='{}'
    width="500"
    height="400"
    html_file="/static/LC1_HandsOnAct.html"
    sop="true"/>
</customresponse>
</problem>
'''

# <codecell>


