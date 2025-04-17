setup() {
  bats_load_library bats-assert
  docker run --name python_app -p 5000:5000 -d --rm tremplin-image:latest
  sleep 10
}

teardown(){
  echo "tests Ended"
  docker kill python_app
}

@test "Verify that the app is lunched and the API respond with correct response." {
  run curl -o /dev/null -s -w "%{http_code}" http://localhost:5000
  assert_success
  assert_output "200"
  
} 

# Passer sur un compose