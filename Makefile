# docker run --rm -e ACCEPT_EULA=Y mcr.microsoft.com/mssql/server:2019-CU18-ubuntu-20.04

password := reallyStrongPwd123
server_name := mysqldocker

launch-docker-sql:
	docker run -d \
		--name $(server_name) -e 'ACCEPT_EULA=Y' \
		-e 'SA_PASSWORD=$(password)' -p 1433:1433 mcr.microsoft.com/azure-sql-edge

start-sql:
	mssql -u sa -p $(password)

docker-stop:
	docker stop

docker-restore-data:
	sudo docker exec -it $(server_name) -p $(password) mkdir /myDatabase
	# cd ~
	# curl -L -o

start-docker:
	docker run \
		--env 'ACCEPT_EULA=Y' \
		--env 'SA_PASSWORD=$(password)' \
		--name '$(server_name)' \
		--hostname '$(server_name)' \
		--publish 1433:1433 \
		--volume $(server_name):/var/opt/mssql \
		--platform linux/amd64 mcr.microsoft.com/mssql/server:2022-RTM-ubuntu-20.04 \
		--detach
# colima start --mount-type=virtiofs --vz-rosetta --arch x86_64 --vm-type=vz
# docker build -t mysqldocker . --platform linux/amd64 --build-arg="SA_PASSWORD=$(password)" 
# docker run -p 1433:1433 --rm -it --entrypoint bash mysqldocker --platform linux/amd64

copy-db:
	docker cp AdventureWorks2022.bak mysqldocker:/var/opt/mssql/data/AdventureWorks2022.bak
	docker run $(server_name) ls /var/opt/mssql/data/

start-docker-bash:
	docker run -it -l /tmp --entrypoint /bin/bash $(server_name)

