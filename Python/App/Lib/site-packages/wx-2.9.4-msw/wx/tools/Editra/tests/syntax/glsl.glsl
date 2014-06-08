// Syntax Highlighting Test File for GLSL
// Comment Text

#define MAX_JOINT_NUM 36
#define MAX_LIGHT_NUM 8

uniform mat4 JointTransform[MAX_JOINT_NUM];

void main() 
{
    int index;
    float dist;
    mat4 ModelTransform = gl_ModelViewProjectionMatrix;
    index = int(gl_Color.r * 255.99);
    mat4 vertTran = JointTransform[index - 1];
    index = int(gl_Color.g * 255.99);
    if(index > 0)
        vertTran += JointTransform[index - 1];
}
