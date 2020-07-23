local likocam = Library("likocam")

local c = likocam.new()

local cube = {
 {{-1,-1,-1}, {-1,1,-1}, {-1,1,1}, {-1,-1,1}},
 {{-1,-1,-1}, {1,-1,-1}, {1,-1,1}, {-1,-1,1}},
 {{-1,-1,-1}, {1,-1,-1}, {1,1,-1}, {-1,1,-1}},
 {{1,1,1}, {1,1,-1}, {1,-1,-1}, {1,-1,1}},
 {{1,1,1}, {-1,1,1}, {-1,1,-1}, {1,1,-1}},
 {{1,1,1}, {-1,1,1}, {-1,-1,1}, {1,-1,1}}
}

local rotspeed = 1
local zspeed = 1
local flspeed = 1

function _draw()
 clear()
 
 color(12)
 c:object(cube)
end

function _update(dt)
 if btn(1) then --left
  c.theta = c.theta - rotspeed*dt
 end
 
 if btn(2) then --right
  c.theta = c.theta + rotspeed*dt
 end
 
 if btn(3) then --up
  c.focallength = c.focallength + flspeed*dt
 end
 
 if btn(4) then --down
  c.focallength = c.focallength - flspeed*dt
 end
 
 if btn(5) then --zoom in
  c.z = c.z + zspeed*dt
 end
 
 if btn(6) then --zoom out
  c.z = c.z - zspeed*dt
 end
end