# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%%html
<!-- Jxg Box -->
<div id='jxgbox1' class='jxgbox' style='width:500px; height:350px; float:left; border: solid #1f628d 2px;'></div>        

<!-- Menu -->
<div id="menu" style="width: 170px; float: left;">
      <ul>
          Add Forces
          <input class="btn" type="button" value="Normal" onClick="var vN = addNormal()">
          <input class="btn" type="button" value="Gravitational" onClick="addGravitational()">
          <input class="btn" type="button" value="Friction" onClick="addFriction()">
          <br></br>

          <input class="btn" type="button" value="Clear" onClick="clearAll()">
          <input class="btn" type="button" value="Console Log State" onClick="fetchState()">
      </ul>
</div>

# <codecell>

%%javascript
// We load the d3.js library from the Web.
require.config({paths: {jsx: "https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore"}});
require(["jsx"], function(jsx) {
    initBoard();
    
    function initBoard() {
        var bboxlimits = [-10, 10, 10, -10];
        var board = JXG.JSXGraph.initBoard('jxgbox1', {boundingbox: [-10, 10, 10, -10], axis:false, showCopyright: false});
    
        var im = board.create('image',["https://studio.edge.edx.org/c4x/DavidsonNext/Ann101/asset/simple_car.png", [bboxlimits[0],bboxlimits[3]], [(bboxlimits[1]-bboxlimits[0]),1.2*(bboxlimits[3]-bboxlimits[2])] ],{fixed:true});
    
        var cm = board.create('point',[0,1.5],{size:1,fixed:true,name:'cm',withLabel:false,strokeColor:'pink',fillColor:'pink'})
    
        return board;
    }

    // Create a vector providing two points.
    function addNormal() {
        vN = createVector('N',[3,1],[5,5]); 
    }
    
});

# <codecell>

answer = {"cm":{"p1":[0,1.5]},"N":{"name":"N","tail":[3,1],"p2":[5,5],"length":4.47213595499958,"angle":63.43494882292201},"g":{"name":"g","tail":[0.03174603174603147,1.4519774011299402],"p2":[0.03968253968253982,-2.485875706214689],"length":3.937861105115565,"angle":-89.88452393201636},"f":{"name":"f","tail":[0.03968253968253954,1.4519774011299436],"p2":[-3.3333333333333335,1.4689265536723164],"length":3.373058456859136,"angle":179.7120954154457}}

# <codecell>

import json
class Vector(object):
    def __init__(self,name,length,angle,tail):
        self.name = name
        self.length = length
        self.angle = angle
        self.tail = tail
        return None

class gradeVector:
    def __init__(self):
        return None

    def compareLengths(self,v1,v2):
        if abs(v1.length-v2.length) < 1.00:
            return True
        else:
            return False

    def checkAngle(self,v1,GIVEN,**kwargs):
        tol = kwargs.get('tol', 1.0)
        if abs(v1.angle - GIVEN) < tol:
            return True
        else:
            return False

    def checkCenterMass(self, cm, vectors, **kwargs):
        tol = kwargs.get('tol', 0.25)
        numFalse = []
        for v in vectors:
            dist = math.hypot(cm[0] - v.tail[0], cm[1] - v.tail[1])
            if dist > tol:
                numFalse.append([v.name,dist])

        if len(numFalse) == 0:
            return True
        else:
            return False


#answer = json.loads(json.loads(ans)['answer'])
cm = answer['cm']['p1']
vN = Vector(answer['N']['name'],answer['N']['length'],answer['N']['angle'],answer['N']['tail'])
vg = Vector(answer['g']['name'],answer['g']['length'],answer['g']['angle'],answer['g']['tail'])
vf = Vector(answer['f']['name'],answer['f']['length'],answer['f']['angle'],answer['f']['tail'])

if gradeVector().compareLengths(vN, vg) == False:
    print {'ok': False, 'msg': 'Normal Force and Gravitational Force should be similar lengths.'}

if gradeVector().checkAngle(vN, 90.0, tol=2.0) == False:
    print {'ok': False, 'msg': 'The angle of the Normal Force is incorrect. Your angle: %.1f' % vN.angle}

if gradeVector().checkAngle(vg, 270.0, tol=2.0) == False:
    print {'ok': False, 'msg': 'The angle of the Gravitational Force is incorrect. Your angle: %.1f' % vg.angle}

if gradeVector().checkAngle(vf, 180.0, tol=2.0) == False:
    print {'ok': False, 'msg': 'The angle of the Frictional Force is incorrect. Your angle: %.1f' % vf.angle}

if gradeVector().checkCenterMass(cm,[vN,vg],tol=0.25) == False:
    print {'ok': False, 'msg': 'One or more of your vectors do not start from the center of mass.'}

    print {'ok': True, 'msg': 'Good job!'}

# <codecell>


