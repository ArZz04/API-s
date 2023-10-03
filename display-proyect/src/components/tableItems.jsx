import React, { useEffect, useState } from 'react';
import Table from 'react-bootstrap/Table';
import fetchData from '../../api/axios';
import CustomPagination from './tablesPagination'; // Importa el componente de paginación

function TableItems() {
  const [data, setData] = useState([]); // Estado para almacenar los datos de la API
  const [loading, setLoading] = useState(true); // Estado para controlar el estado de carga
  const [sortField, setSortField] = useState('nombre'); // Campo de orden inicial
  const [sortOrder, setSortOrder] = useState('asc'); // Dirección de orden inicial
  const [currentPage, setCurrentPage] = useState(1); // Página actual
  const [itemsPerPage] = useState(20); // Cantidad de elementos por página (ajusta según tus necesidades)

  useEffect(() => {
    // Define la función para cargar los datos de la API
    async function fetchDataFromApi() {
      try {
        // Llama a la función fetchData para obtener los datos de la API
        const response = await fetchData('http://0.0.0.0:8000/sqlite/items'); // Especifica la URL completa

        setData(response); // Almacena los datos de la respuesta en el estado
        setLoading(false); // Cambia el estado de carga a falso una vez que se han cargado los datos
      } catch (error) {
        console.error('Error:', error);
        setLoading(false); // Cambia el estado de carga a falso en caso de error
      }
    }

    fetchDataFromApi(); // Llama a la función para cargar los datos de la API cuando el componente se monta
  }, []); // El segundo argumento [] asegura que esta función se ejecute solo una vez al montar el componente

  // Función para cambiar el campo y la dirección de ordenamiento
  const handleSort = (field) => {
    if (field === sortField) {
      // Si el mismo campo se hace clic nuevamente, cambia la dirección de orden
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      // Si se hace clic en un campo diferente, establece el nuevo campo y la dirección ascendente
      setSortField(field);
      setSortOrder('asc');
    }
  };

  // Función para ordenar los datos en función del campo y la dirección de ordenamiento
  const sortedData = data.sort((a, b) => {
    const compareValue = a[sortField].localeCompare(b[sortField]);
    return sortOrder === 'asc' ? compareValue : -compareValue;
  });

  // Paginación
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = sortedData.slice(indexOfFirstItem, indexOfLastItem);
  const dataWithProductNumbers = currentItems.map((item, index) => ({
    ...item,
    productNumber: index + 1 + (currentPage - 1) * itemsPerPage,
  }));

  const totalPages = Math.ceil(sortedData.length / itemsPerPage);

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  return (
    <div className="table-container">
      <h1 className='text-title'>Tabla de Productos</h1>

      {loading ? (
        <p>Cargando datos...</p>
      ) : (
        <>
          <Table responsive className="custom-table">
            <thead className='text-head'>
              <tr>
                <th>#</th>
                <th onClick={() => handleSort('nombre')} className="sortable">
                  Nombre {sortField === 'nombre' && (sortOrder === 'asc' ? '▲' : '▼')}
                </th>
                <th onClick={() => handleSort('plu')} className="sortable">
                  PLU {sortField === 'plu' && (sortOrder === 'asc' ? '▲' : '▼')}
                </th>
                <th>Precio</th>
              </tr>
            </thead>
            <tbody className='text-body'>
              {dataWithProductNumbers.map((item, index) => (
                <tr key={index}>
                  <td>{item.productNumber}</td>
                  <td>{item.nombre}</td>
                  <td>{item.plu}</td>
                  <td>{item.precio}</td>
                </tr>
              ))}
            </tbody>
          </Table>
          <CustomPagination
            activePage={currentPage}
            totalPages={totalPages}
            onPageChange={handlePageChange}
          />
        </>
      )}
    </div>
  );
}

export default TableItems;
