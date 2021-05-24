1.0 This is dockerized nmap test execution version 1.0.0 

2.0 this will contain following basic files:
	docker-file
	docker-compose.yml 
	python file
	settings.ini
	nmap_test_plan.xls

3.0 How to execute the test:
	a. Install doocker for desktop in windows / install docker in linux flavour machine. 
	b. Get all the basic files listed in 2.0
	c. then open settings.ini file and type the IP address of the target device, test plan name and sheet name
	d. change the volume to store the generated files in docker-compose.yml file (optional)
	e. Then open command promt and navigate to the directory where all the files are located.
	f. Then excute the following command "docker-compose up"
	