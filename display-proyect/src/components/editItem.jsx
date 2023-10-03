// EditItem.jsx

import React, { useState, useEffect } from 'react';
import './css/editItem.css'; // Importa los estilos CSS

function EditItem({ itemId, itemName, itemDescription, onSave }) {
  const [name, setName] = useState(itemName);
  const [description, setDescription] = useState(itemDescription);

  const handleSave = () => {
    // Aquí puedes realizar alguna lógica de validación o procesamiento antes de guardar
    // Por ejemplo, puedes enviar una solicitud de actualización al servidor
    onSave(itemId, name, description);
  };

  return (
    <div className="edit-item-container">
      <h2 className="edit-item-title">Editar Elemento</h2>
      <div>
        <label htmlFor="name" className="edit-item-label">Nombre:</label>
        <input
          type="text"
          id="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="edit-item-input" /* Aplica el estilo del campo de entrada */
        />
      </div>
      <div>
        <label htmlFor="description" className="edit-item-label">Descripción:</label>
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="edit-item-textarea"/>
          </div>
      <button onClick={handleSave} className="edit-item-button">Guardar</button>
    </div>
  );
}

export default EditItem;
