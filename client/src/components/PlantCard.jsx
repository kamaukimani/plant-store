import { useState } from "react";

function PlantCard({ plant,onDeletePlant}) {
  const { id,name, image, price } = plant;
  //console.log(id)

  const [isInStock, setIsInStock] = useState(true);

  function handleToggleStock() {
    setIsInStock((isInStock) => !isInStock);
  }
  function handleDelete(){
    //console.log("I have been clicked")
    fetch(`/plants/${id}`,{
      method:"DELETE"
    })
    .then(r=>r.json())
    .then(message=>{
      console.log(message)
      onDeletePlant(id)
    })
  }

  return (
    <li className="card">
      <img src={image} alt={name} />
      <h4>{name}</h4>
      <p>Price: {price}</p>
      <button onClick={handleDelete}>🗑</button> <br/>
      {isInStock ? (
        <button className="primary" onClick={handleToggleStock}>
          In Stock
        </button>
      ) : (
        <button onClick={handleToggleStock}>Out of Stock</button>
      )}
    </li>
  );
}

export default PlantCard;
