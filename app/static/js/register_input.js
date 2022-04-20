const inputPassword = document.getElementById('password')
const inputConfirmPassword = document.getElementById('password_confirmation')
const submitForm = document.getElementById('form')

const checkMatchPasswords = (password, confirmPassowrd) => {
  if (password != confirmPassowrd) {
    return false
  }

  return true
}