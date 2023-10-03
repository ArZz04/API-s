import axios from 'axios';

// Función para realizar una solicitud GET a una API y devolver los datos
async function fetchData(apiEndpoint, queryParams) {
  try {
    const response = await axios.get(apiEndpoint, {
      params: queryParams,
    });
    return response.data; // Devuelve los datos de la respuesta
  } catch (error) {
    throw error; // Lanza el error si ocurre uno
  }
}

export default fetchData;