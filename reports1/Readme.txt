1.0 This is dockerized nmap test execution:

2.0 this will contain basic files:
	docker for desktop windows app / install docker in linux machine
	docker-file
	docker-compose.yml 
	python file
	settings.ini
	nmap_test_plan.xls

3.0 How to execute the test:
	Get all the basic files listed in 2.0
	then open settings.ini file and type the IP address. test plan name and sheet name
	change the volume to store the generated files in docker-compose.yml file
	then open command promt and navigate to the directory where all the files are located.
	then excute the following command "docker-compose up"
	