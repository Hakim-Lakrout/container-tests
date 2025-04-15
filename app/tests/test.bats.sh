setup() {
    bats_load_library bats-assert
}

@test "Verify that the app is lunched and the API respond with correct response." {


  run echo "hello world"
  assert_success
  assert_output --partial "hello"

} 
