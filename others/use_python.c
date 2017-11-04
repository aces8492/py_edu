#include <stdio.h>
#include <python.h>

int main(void) {
	Py_Initialize();
	PyRun_SimpleString("print 'hello python'");
	Py_Finalize();
	return 0;
}
