<template lang="html">
  <div class="container">

    <div class="row">
      <div class="col text-left">
        <h2>Editar Producto</h2>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">

            <form @submit="onSubmit">

              <div class="form-group row">
                <label for="title" class="col-sm-2 col-form-label">Nombre</label>
                <div class="col-sm-6">
                  <input type="text" placeholder="Nombre" name="title" class="form-control" v-model.trim="form.nombre">
                </div>
              </div>

              <div class="form-group row">
                <label for="title" class="col-sm-2 col-form-label">Precio</label>
                <div class="col-sm-6">
                  <input type="text" placeholder="Precio" name="precio" class="form-control" v-model.trim="form.precio">
                </div>
              </div>

              <div class="form-group row">
                <label for="description" class="col-sm-2 col-form-label">Descripción</label>
                <div class="col-sm-6">
                  <textarea name="description" class="form-control" placeholder="Descripción" rows="3" v-model.trim="form.descripcion">
                  </textarea>
                </div>
              </div>
              <div class="rows">
                <div class="col text-left">
                  <b-button type="submit" variant="primary">Editar</b-button>
                  <b-button type="submit" class="btn-large-space" :to="{ name: 'ProductList' }">Cancelar</b-button>
                </div>
              </div>

            </form>

          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>

import axios from 'axios'
import swal from 'sweetalert'

export default {
  data() {
    return {
      productId: null,
      form: {
        nombre: '',
        precio: '',
        descripcion: ''
      },
      allProduct: [],
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()

      const path = `http://127.0.0.1:8000/update_product/${this.productId}/`

      axios.put(path, this.form).then((response) => {
        this.form.nombre = response.data.nombre
        this.form.precio = response.data.precio
        this.form.decripcion = response.data.descripcion

        swal("Producto actualizado existosamente!", "", "success")
      })
      .catch((error) => {
        console.log(error)
      })
      
    },

    getProduct (){
      const path = `http://127.0.0.1:8000/all_product/`

      axios.get(path).then((response) => {
        this.allProduct = response.data.allProducts
        this.allProduct.forEach(product => {
          if (product.id === this.productId) {
            this.form.nombre  = product.nombre;
            this.form.precio = product.precio;
            this.form.descripcion = product.descripcion;
          }
        });

      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  created() {
    this.getProduct()
    this.productId = this.$route.params.productId;
  }
}
</script>

<style lang="css" scoped>
</style>
