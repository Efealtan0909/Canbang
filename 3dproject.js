class Vector {
	x = 0
	y = 0
	z = 0
	constructor(x = 0, y = 0, z = 0) {
		this.x = x;
		this.y = y;
		this.z = z;
	}
}

class Vector2 {
	x = 0
	y = 0
	constructor(x = 0, y = 0) {
		this.x = x;
		this.y = y;
	}
}

const a = new Vector(1, 1, 1);

const c = new Vector(1, 1, 1);

const O = new Vector(1, 1, 1);

const e = new Vector(1, 1, 1);

const X = a.x - c.x;
const Y = a.y - c.y;
const Z = a.z - c.z;

const Cx = Math.cos(O.x);
const Cy = Math.cos(O.y);
const Cz = Math.cos(O.z);

const Sx = Math.sin(O.x);
const Sy = Math.sin(O.y);
const Sz = Math.sin(O.z);

const CxX = Cx * X;
const CxY = Cx * Y;
const CxZ = Cx * Z;

const CyX = Cy * X;
const CyY = Cy * Y;
const CyZ = Cy * Z;

const CzX = Cz * X;
const CzY = Cz * Y;
const CzZ = Cz * Z;

const SxX = Sx * X;
const SxY = Sx * Y;
const SxZ = Sx * Z;

const SyX = Sy * X;
const SyY = Sy * Y;
const SyZ = Sy * Z;

const SzX = Sz * X;
const SzY = Sz * Y;
const SzZ = Sz * Z;

const d = new Vector(
	Cy * (SzY + CzX) - SyZ,
	Sx * (CyX + Sy * (SzY + CzX)) + Cx * (CzY - SzX),
	Cx * (CyZ + Sy * (SzY + CzX)) - Sx * (CzY - SzX)
)

console.log(d);

const b = new Vector2(
	(e.z / d.z) * d.x + e.x,
	(e.z / d.z) * d.y + e.y
)

console.log(b)

setTimeout(() => {
	console.log('illegal');
}, 100000000)