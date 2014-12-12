# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import HTML

# <markdowncell>

# #Diluting Gravity

# <codecell>

%%HTML
<!DOCTYPE html>
<html>
    <head>
        <style> 
            body {
                margin: 10px;
            }
            #jxgbox1 {  
                border:1px solid black; background-size: contain; background-repeat: no-repeat;
                background-position: center; background-size: 80% auto;
            }
            
        </style>

    </head>


    <body>       
        <!-- Jxg Box -->
        <div id='jxgbox1' class='jxgbox' style='width:500px; height:350px; float:left; border: solid #1f628d 2px;'></div>        
        
        <!-- Menu -->
        <div id="menu" style="width: 170px; float: left;">
              <ul>
                  Add Forces
                  <input class="btn" type="button" value="Reset Cart" onClick="resetCart()">
                  <br></br>

                  <input class="btn" type="button" value="Clear" onClick="clearAll()">
              </ul>
          </div>

        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>
        <script type='text/javascript'>
            
            var board = JXG.JSXGraph.initBoard('jxgbox1', {boundingbox: [-10, 10, 10, -10], axis:true, showCopyright: false});
            
            //Air-Track
            track = [];
            var pL = board.create('point',[-8,1], {visible: false})
            var pR = board.create('point',[8,1], {visible: false})
            var track = board.create('segment', [pL, pR], {visible: true});
            
            isInDragMode = false;
            
            //Adjust Height
            var h = board.create('slider', [[-1,-1],[2,-1],[0,0,-(1.0/12)*Math.PI]],{name:'angle'});
            var tRot = board.create('transform', [function(){return h.Value();}, pR], {type:'rotate'}); 
            tRot.bindTo(pL);
            
            //Glider
            cart = board.create('glider', [-8, -7, track], {name: 'Weight', withLabel:false, face:'[]', size:10});
            //rectangular cart: http://jsxgraph.uni-bayreuth.de/wiki/index.php/Grouping_objects
            
            //Animation
            function startAnimation(startX) {
                point.moveAlong(function() {
                    var f = function(t, x) {
                            var k = 0.5, m = 1;
                            return [x[1], - k / m * x[0]];
                        },
                        area = [0, 200],
                        numberOfEvaluations = (area[1] - area[0]) * 100,
                        data = JXG.Math.Numerics.rungeKutta('heun', [startX, 0], area, numberOfEvaluations, f),
                        duration = 20 * 1e3;

                    return function(t) {
                        if (t >= duration)
                            return NaN;

                        return [0, data[Math.floor(t / duration * numberOfEvaluations)][0]];
                    }
                }());
            }

            function hook() {
                if(!isInDragMode) {
                    if(board.mode === board.BOARD_MODE_DRAG) {
                        board.stopAllAnimation();
                        isInDragMode = true;
                    }
                }

                if(isInDragMode) {
                    if(board.mode !== board.BOARD_MODE_DRAG) {
                        isInDragMode = false;
                        startAnimation(cart.X());
                    }
                }
            }
            board.addHook(hook);
            startAnimation(0);
            
                                    
            

        </script>
    </body>
</html>


# <codecell>

def vglcfn(e, ans):
  '''
  Grading a force diagram.
  '''
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


  answer = json.loads(json.loads(ans)['answer'])
  cm = answer['cm']['p1']
  if 'N' in answer and 'g' in answer and 'f' in answer:
      vN = Vector(answer['N']['name'],answer['N']['length'],answer['N']['angle'],answer['N']['tail'])
      vg = Vector(answer['g']['name'],answer['g']['length'],answer['g']['angle'],answer['g']['tail'])
      vf = Vector(answer['f']['name'],answer['f']['length'],answer['f']['angle'],answer['f']['tail'])
  else:  
      return {'ok': False, 'msg': 'You need to use all three vectors.'}

  if gradeVector().compareLengths(vN, vg) == False:
      return {'ok': False, 'msg': 'Normal Force and Gravitational Force should be similar lengths.'}

  if gradeVector().checkAngle(vN, 90.0, tol=2.0) == False:
      return {'ok': False, 'msg': 'The angle of the Normal Force is incorrect. Your angle: %.1f' % vN.angle}

  if gradeVector().checkAngle(vg, 270.0, tol=2.0) == False:
      return {'ok': False, 'msg': 'The angle of the Gravitational Force is incorrect. Your angle: %.1f' % vg.angle}

  if gradeVector().checkAngle(vf, 180.0, tol=2.0) == False:
      return {'ok': False, 'msg': 'The angle of the Frictional Force is incorrect. Your angle: %.1f' % vf.angle}

  if gradeVector().checkCenterMass(cm,[vN,vg],tol=0.25) == False:
      return {'ok': False, 'msg': 'One or more of your vectors do not start from the center of mass.'}

  return {'ok': True, 'msg': 'Good job!'}

# <codecell>


