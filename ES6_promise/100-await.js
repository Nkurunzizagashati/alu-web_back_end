import { uploadPhoto, createUser } from "./utils.js";

const response_from_uploadPhoto_function = await uploadPhoto();
const response_from_createUser_function = await createUser();
if (uploadedPhoto && createdUser) {
  return {
    photo: response_from_uploadPhoto_function,
    user: response_from_createUser_function,
  };
}

return {
  photo: null,
  user: null,
};
