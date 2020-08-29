#include <iostream>
#include <cstdlib>
#include "thread.h"

using std::cout;
using std::endl;

mutex m;

void child2(void *a) {
	cout << "something " << endl;
	for (int i=0; i<100; ++i) {
		cout << "c2";
	}
	cout << " done" << endl;
}

void child(void *a) {
	char *id = (char *) a;
  thread t2 ( (thread_startfunc_t) child2, (void *) "second child");
	t2.join(); // waitijng for child2 to finish
	cout << "should not display before child2 is done" << endl;
	cout << "should not display before child2 is done" << endl;
}

void parent(void* a) {
	cout << "parent called with " << (int64_t) a << endl;
	thread t1 ( (thread_startfunc_t) child, (void *) "child thread");
	for (int i = 0; i < 3; ++i){
		thread t((thread_startfunc_t) child, (void *) "child ");
		t.join();
		cout << " I yield my son!" << endl;
		thread::yield();
	}
	cout << "done son" << endl;
}

int main() {
	cpu::boot(1,(thread_startfunc_t)parent, (void*)100, false, false, 0);
}
