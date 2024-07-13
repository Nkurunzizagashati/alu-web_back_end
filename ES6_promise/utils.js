// 100-await.js
import { uploadPhoto, createUser } from "./utils";

async function asyncUploadUser() {
  try {
    const response_from_uploadPhoto_function = await uploadPhoto();
    const response_from_createUser_function = await createUser();
    return {
      photo: response_from_uploadPhoto_function,
      user: response_from_createUser_function,
    };
  } catch (error) {
    return { photo: null, user: null };
  }
}

asyncUploadUser();
