def install():
	try:
		subprocess.run(["pip", "install"," NAT"], check=True)
		subprocess.run(["pip", "install"," BAT"], check=True)
		subprocess.run(["pip", "install"," CAT"], check=True)
		     
	except subprocess.CalledProcessError as e:
		print(f"Error: {e}")
		sys.exit(1)
	print("Updated with Message:"+commit_message)

install()
