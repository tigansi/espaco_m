import { http } from "./config";

export default {
  provider: (api, dados) => {
    return http.post(api, dados, { timeout: 4000 });
  },
};
