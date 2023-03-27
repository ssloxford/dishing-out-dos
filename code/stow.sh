# Send an HTTP POST request containing a gRPC command to ``stow'' the dish, turning it away from the sky

printf '\x00\x00\x00\x00\x03\x92}\x00' \
| curl 'http://192.168.100.1:9201/SpaceX.API.Device.Device/Handle' \
-X POST \
-H 'Accept: */*' \
-H 'Accept-Language: en-GB,en;q=0.5' \
-H 'content-type: application/grpc-web+proto' \
-H 'x-grpc-web: 1' \
--data-binary @- -v | xxd
