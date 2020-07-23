function cos(n) {
    return Math.cos(n);
}

function sin(n) {
    return Math.sin(n);
}

const theta = 1;

const z = -3;

const focallength = 5;

function _perspective (p) {
    const [x,y,z] = p
    const x_rot = x * cos(theta) - z * sin(theta)
    const z_rot = x * sin(theta) + z * cos(theta)
    const dz = z_rot - z
    const out_z = z + focallength
    const m_xz = x_rot / dz
    const m_yz = y / dz
    const out_x = m_xz * out_z
    const out_y = m_yz * out_z
    return {
        out_x,
        out_y
    }
}

console.log(_perspective([1, 1, 1]));