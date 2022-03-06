import rhinoscriptsyntax as rs

pts = {}

tower_radius = rs.GetInteger('tower radius : ',20)
intervals = rs.GetInteger('intervals :',15)
lenghts_tower = rs.GetInteger('Length :',75)
#Build the tower 

circle_bottom = rs.AddCircle((0,0,0), tower_radius)
circle_top = rs.AddCircle((0,0,lenghts_tower),tower_radius)

tower = rs.AddLoftSrf((circle_bottom, circle_top))

ud = rs.SurfaceDomain(tower, 0)
vd = rs.SurfaceDomain(tower, 1)

step_u = (ud[1] - ud[0])/intervals
step_v = (vd[1] - vd[0])/intervals

for i in range(intervals+1) :
    for j in range(intervals+1) :
        
        u = ud[0] + step_u * i
        v = vd[0] + step_v * j

        point = rs.EvaluateSurface(tower,u,v)
        
        pts[(i,j)] = point
        #rs.AddTextDot((i,j), point)
        
        
for i in range(intervals+1) :
    for j in range(intervals+1) :
        if i > 0 and j > 0 :
            right_line = rs.AddCurve((pts[(i,j)], pts[(i-1,j-1)]))
            left_line = rs.AddCurve((pts[(i,j)], pts[(i+1,j-1)]))
            
            rs.ObjectColor(right_line,(255/intervals*i, 255-(255/intervals)*j,255/(j*intervals)))
            mat_index = rs.AddMaterialToObject(right_line)
            rs.MaterialColor(mat_index, (255/intervals*i, 255-(255/intervals)*j,255/(j*intervals)))
            
            rs.ObjectColor(left_line,(255/intervals*i, 255-(255/intervals)*j,255/(j*intervals)))
            mat_index = rs.AddMaterialToObject(left_line)
            rs.MaterialColor(mat_index, (255/intervals*i, 255-(255/intervals)*j,255/(j*intervals)))
