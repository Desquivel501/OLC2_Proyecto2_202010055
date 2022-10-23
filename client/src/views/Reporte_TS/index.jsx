import React, { useEffect, useState } from "react";
import Table from 'react-bootstrap/Table'

export const Reporte_TS = () => {

    const [simbolo, setSimbolos] = useState(null)

    useEffect(() => {
        getemployees()
    }, [])

    const getemployees = () => {
      fetch("http://127.0.0.1:5000/simbolos", {
          method: 'GET',
          headers: {
            'Content-Type':'application/json'
          }
        })
          .then(res => res.json())
          .then(
              (result) => {                    
                setSimbolos(result)
              },
              (error) => {
                setSimbolos(null);
              }
          )
   }

  if (!simbolo) return (<h1 className='text-white mb-4 mt-4'>No se ha encontrado Tabla de Simbolos</h1>)

  return (
      <div className='justify-content-start'>
        <h1 className='text-white mb-4 mt-4'>Reporte Tabla de Simbolos</h1>


          <Table striped bordered hover variant="dark">
            <thead>
              <tr>
                <th>Nombre</th>
                <th>Tipo</th>
                <th>Ambito</th>
                <th>Linea</th>
                <th>Columna</th>
              </tr>
            </thead>
            <tbody>

              {simbolo.map(sim => (
                    <tr>
                        <td>{sim.id}</td>
                        <td>{sim.tipo}</td>
                        <td>{sim.ambito}</td>
                        <td>{sim.linea}</td>
                        <td>{sim.columna}</td>
                    </tr>
                ))}
              
            </tbody>
          </Table>


      </div>
    )
  }
  