#!/bin/bash
setup() {
  bats_load_library bats-assert
  docker run --name python_app -p 5002:5000 -d --rm tremplin-image:latest
  sleep 10
}

teardown(){
  echo "tests Ended"
  docker kill python_app
}

@test "Verify that the app is launched and the API respond with correct response." {
  run curl -o /dev/null -s -w "%{http_code}" http://localhost:5002/me.html
  assert_success
  assert_output "200"
  
} 