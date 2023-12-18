# Put common setup steps in an initial stage
# FROM mcr.microsoft.com/mssql/server:2022-RTM-ubuntu-20.04 AS setup
# FROM mcr.microsoft.com/mssql/server:2019-latest AS setup

# Have a stage specifically to populate the data directory
# FROM setup AS data
# (copy-and-pasted from the question)
USER mssql
COPY AdventureWorks2022.bak /AdventureWorks2022.bak
RUN ( /opt/mssql/bin/sqlservr & ) | grep -q "Service Broker manager has started" \
    && /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P $SA_PASSWORD -Q 'RESTORE DATABASE AdventureWorks2022 FROM DISK = "/var/opt/mssql/data/AdventureWorks2022.bak" WITH COPY "AdventureWorks20022" to "/var/opt/mssql/data/AdventureWorks2022.mdf", MOVE "AdventureWorks2022_Log" to "/var/opt/mssql/data/AdventureWorks2022_log.ldf", NOUNLOAD, STATS = 5' \
    && pkill sqlservr

# Final stage that actually will actually be run.
FROM setup
# Copy the prepopulated data tree, but not the backup file
COPY --from=data /var/opt/mssql /var/opt/mssql
# Use the default USER, CMD, etc. from the base SQL Server image