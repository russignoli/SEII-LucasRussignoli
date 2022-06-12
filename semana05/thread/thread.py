import time

start = time.perf_counter()
def do_something():
	print('Sleeping for 01 second...')
	time.sleep(1)
	print('Done sleeping...')
do_something()
do_something()
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import time
import threading
start = time.perf_counter()
def do_something():
	print('Sleeping for 01 second...')
	time.sleep(1)
	print('Done sleeping...')
t1 = threading.thread(target= do_something)
t2 = threading.thread(target= do_something)
t1.start()
t2.start()
t1.join()
t2.join()
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import time
import threading
start = time.perf_counter()
def do_something():
	print('Sleeping for 01 second...')
	time.sleep(1)
	print('Done sleeping...')
threads = []
for _ in range(10):
	t = threading.Thread(target= do_something)
	t.start()
	threads.append(t)
for thread in threads:
	thread.join()
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import time
import threading
start = time.perf_counter()
def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	print('Done sleeping...')
threads = []
for _ in range(10):
	t = threading.Thread(target= do_something, args =[1.5])
	t.start()
	threads.append(t)
for thread in threads:
	thread.join()
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')

import time
import concurrent.futures
start = time.perf_counter()
def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	return 'Done sleeping...'
with concurrent.futures.ThreadPoolExecutor() as executor:
	f1 = executor.submit(do_something, 1)
	f2 = executor.submit(do_something, 1)
	print(f1.result())
	print(f2.result())
#threads = []
#for _ in range(10):
#	t = threading.Thread(target= do_something, args =[1.5])
#	t.start()
#	threads.append(t)
#
#for thread in threads:
#	thread.join()
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import time
import concurrent.futures
start = time.perf_counter()
def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	return 'Done sleeping...'
with concurrent.futures.ThreadPoolExecutor() as executor:
	results = [executor.submit(do_something, 1) for _ in range(10)] 
	
	for f in concurrent.futures.as_completed(results):
		print(f.result())
#threads = []
#for _ in range(10):
#	t = threading.Thread(target= do_something, args =[1.5])
#	t.start()
#	threads.append(t)
#
#for thread in threads:
#	thread.join()
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import time
import concurrent.futures
start = time.perf_counter()
def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	return (f'Done sleeping {seconds}...')
with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [5, 4, 3, 2, 1]
	results = [executor.submit(do_something, sec) for sec in secs] 
	
	for f in concurrent.futures.as_completed(results):
		print(f.result())
#threads = []
#for _ in range(10):
#	t = threading.Thread(target= do_something, args =[1.5])
#	t.start()
#	threads.append(t)
#
#for thread in threads:
#	thread.join()
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	return (f'Done sleeping {seconds}...')

with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [5, 4, 3, 2, 1]
	results = executor.map(do_something, secs)
	
	for result in results:
		print(result)

#threads = []

#for _ in range(10):
#	t = threading.Thread(target= do_something, args =[1.5])
#	t.start()
#	threads.append(t)
#
#for thread in threads:
#	thread.join()


finished = time.perf_counter()

print(f'Finished in {round(finished - start, 2)} second(s)')
"""