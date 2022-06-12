
import asyncio
async def main():
	print('tim')
asyncio.run(main())

"""
import asyncio
async def main():
	print('tim')
	await foo('text')
async def foo(text):
	print(text)
	await asyncio.sleep(5)
asyncio.run(main())
"""
"""
import asyncio
async def main():
	print('tim')
	await foo('text')
	print('finished')
async def foo(text):
	print(text)
	await asyncio.sleep(3)
asyncio.run(main())
"""
"""
import asyncio
async def main():
	print('tim')
	task = asyncio.create_task(foo('text'))
	await task
	print('finished')
async def foo(text):
	print(text)
	await asyncio.sleep(3)
"""
"""
import asyncio
async def main():
	print('tim')
	task = asyncio.create_task(foo('text'))
	await asyncio.sleep(3)
	print('finished')
async def foo(text):
	print(text)
	await asyncio.sleep(1)
asyncio.run(main())
"""
"""
import asyncio
async def main():
	print('tim')
	task = asyncio.create_task(foo('text'))
	await asyncio.sleep(0.5)
	print('finished')
async def foo(text):
	print(text)
	await asyncio.sleep(10)
asyncio.run(main())
"""
"""
import asyncio
async def fetch_data():
	print('starting fetching')
	await asyncio.sleep(2)
	print('finishing fetching')
	return{'data':1}
async def print_number():
	for num in range(10):
		print(num)
		await asyncio.sleep(0.25)
async def main():
	task1 = asyncio.create_task(fetch_data())
	task2 = asyncio.create_task(print_number())
	
	value = await task1
	print(value)
asyncio.run(main())
"""
"""
import asyncio
async def fetch_data():
	print('starting fetching')
	await asyncio.sleep(2)
	print('finishing fetching')
	return{'data':1}
async def print_number():
	for num in range(10):
		print(num)
		await asyncio.sleep(0.25)
async def main():
	task1 = asyncio.create_task(fetch_data())
	task2 = asyncio.create_task(print_number())
	
	value = await task1
	print(value)
	await task2
asyncio.run(main())
"""
"""
import asyncio
async def fetch_data():
	print('starting fetching')
	await asyncio.sleep(2)
	print('finishing fetching')
	return{'data':1}
async def print_number():
	for num in range(10):
		print(num)
		await asyncio.sleep(0.25)
async def main():
	await fetch_data()
	task2 = asyncio.create_task(print_number())
	await task2
asyncio.run(main())
"""
"""
import asyncio

async def fetch_data():
	print('starting fetching')
	await asyncio.sleep(2)
	print('finishing fetching')
	return{'data':1}

async def print_number():
	for num in range(10):
		print(num)
		await asyncio.sleep(0.25)

async def main():
	task2 = asyncio.create_task(print_number())
	await fetch_data()
	await task2

asyncio.run(main())
"""