
in vec2 texCoord_interp;
out vec4 fragColor;
#define texture2D texture

uniform float znear;
uniform float zfar;
uniform sampler2D image;

void main()
{
	float depth = texture2D(image, texCoord_interp).r;

	/* normalize */
	fragColor.rgb = vec3((2.0f * znear) / (zfar + znear - (depth * (zfar - znear))));
	fragColor.a = 1.0f;
}
