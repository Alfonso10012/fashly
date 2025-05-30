function toggleForm(formId) {
  let formToShow = document.getElementById(formId);
  let allForms = document.querySelectorAll('.form-overlay1');

  allForms.forEach(form => {
    if (form.id !== formId && form.classList.contains('active')) {
      form.classList.remove('active');
      setTimeout(() => {
        form.style.display = "none";
      }, 600);
    }
  });

  if (formToShow.classList.contains('active')) {
    formToShow.classList.remove('active');
    setTimeout(() => {
      formToShow.style.display = "none";
    }, 600);
  } else {
    formToShow.style.display = "block";
    setTimeout(() => {
      formToShow.classList.add('active');
    }, 10);
  }
}

// el fucking footer 
window.addEventListener('scroll', () => {
  const footer = document.getElementById('footer');
  const scrollHeight = document.documentElement.scrollHeight;
  const scrollPosition = window.innerHeight + window.scrollY;

  if (scrollPosition >= scrollHeight - 50) {
    footer.classList.add('visible');
  } else {
    footer.classList.remove('visible');
  }
});

// LOGITOP
document.addEventListener("DOMContentLoaded", function () {
  setTimeout(() => {
    document.getElementById("preloader").classList.add("hidden");
  }, 2000);
});

window.addEventListener("load", () => {
  setTimeout(() => {
    const preloader = document.getElementById("preloader");
    preloader.style.display = "none";
  }, 3000);
});

// Navbar grande -> pequeña al hacer scroll
window.addEventListener('scroll', () => {
  const navbar = document.getElementById('mainNavbar');
  if (window.scrollY > 5) {
    navbar.classList.add('navbar-shrink');
  } else {
    navbar.classList.remove('navbar-shrink');
  }
});

// CARRUSEEEEEELLL
document.addEventListener('DOMContentLoaded', function () {
  const carousel = document.getElementById('heroCarousel');
  const bsCarousel = bootstrap.Carousel.getOrCreateInstance(carousel);

  carousel.addEventListener('click', function (e) {
    const x = e.clientX;
    const width = carousel.offsetWidth;

    if (x < width / 2) {
      bsCarousel.prev();
    } else {
      bsCarousel.next();
    }
  });
});

// 3 ESTILO DE ALERTAS 
setTimeout(() => {
  document.querySelectorAll('.alert').forEach(alert => {
    alert.classList.add('hide');
    alert.addEventListener('animationend', () => alert.remove());
  });
}, 3000);

function agregarAlCarrito(productoId, precio) {
  fetch(`/iCarritto/${productoId}/${precio}`, {
    method: 'GET',
    headers: { 'X-Requested-With': 'XMLHttpRequest' }
  })
    .then(response => response.json())
    .then(data => {
      if (data.ok) {
        const contador = document.getElementById('contador-carrito');
        if (contador) {
          contador.innerText = data.carritto;
        }
      }
    })
    .catch(error => console.error('Error al agregar al carrito:', error));
}

document.addEventListener('DOMContentLoaded', function () {
  const inputBusqueda = document.getElementById('input-busqueda');
  const searchBtn = document.getElementById('btn-buscar');
  const contenedor = document.getElementById('contenedor-resultados');
  const modalBusqueda = new bootstrap.Modal(document.getElementById('modalBusqueda'));

  function realizarBusqueda() {
    const q = inputBusqueda.value.trim();
    if (!q) return;

    fetch(`/buscar?q=${encodeURIComponent(q)}`)
      .then(resp => {
        if (!resp.ok) throw new Error("Error en la respuesta del servidor");
        return resp.json();
      })
      .then(resultados => {
        contenedor.innerHTML = '';
        if (resultados.error) {
          contenedor.innerHTML = `<div class="col-12 text-center text-danger">${resultados.error}</div>`;
        } else if (resultados.length === 0) {
          contenedor.innerHTML = `<div class="col-12 text-center">No se encontraron productos para "<strong>${q}</strong>".</div>`;
        } else {
          resultados.forEach(prod => {
            const col = document.createElement('div');
            col.className = 'col-md-4 mb-3';
            col.innerHTML = `
              <div class="card h-100">
                <img src="/static/img/${prod.imagen}" class="card-img-top" style="object-fit: cover; height: 180px;" alt="${prod.nombre}">
                <div class="card-body d-flex flex-column">
                  <h6 class="card-title">${prod.nombre}</h6>
                  <p class="card-text">${prod.descripcion}</p>
                  <p class="card-text fw-bold">$${prod.precio} MXN</p>
                  <button class="btn btn-sm btn-primary mt-auto" onclick="agregarAlCarrito(${prod.id}, '${prod.precio}')">
                    <i class="fa-solid fa-cart-plus me-1"></i> Agregar
                  </button>
                </div>
              </div>`;
            contenedor.appendChild(col);
          });
        }
        modalBusqueda.show();
      })
      .catch(err => {
        console.error('Error en búsqueda:', err);
        contenedor.innerHTML = `<div class="col-12 text-center text-danger">Error al buscar productos.</div>`;
        modalBusqueda.show();
      });
  }

  searchBtn.addEventListener('click', function () {
    const searchBox = this.closest('.search-box');
    searchBox.classList.add('active');
    inputBusqueda.focus();
  });

  inputBusqueda.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      realizarBusqueda();
    }
  });

  const modalElement = document.getElementById('modalBusqueda');
  modalElement.addEventListener('hidden.bs.modal', () => {
    contenedor.innerHTML = '';
    inputBusqueda.value = '';
    const searchBox = searchBtn.closest('.search-box');
    searchBox.classList.remove('active');
  });
});


document.getElementById('cardNumber').addEventListener('input', function (e) {
    let value = e.target.value.replace(/\D/g, '').substring(0, 16);
    let formatted = value.match(/.{1,4}/g);
    e.target.value = formatted ? formatted.join('-') : '';
});

document.getElementById('expiryDate').addEventListener('input', function (e) {
    let value = e.target.value.replace(/\D/g, '').substring(0, 4);
    if (value.length >= 3) {
        e.target.value = value.substring(0, 2) + '/' + value.substring(2);
    } else {
        e.target.value = value;
    }
});

document.getElementById('btnPagar').addEventListener('click', function (e) {
    e.preventDefault();
    const form = document.getElementById('formPago');

    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }

    fetch('/procesar_pago', {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const modal = new bootstrap.Modal(document.getElementById('modalPagoExitoso'));
            modal.show();

            // Vaciar carrito en la UI
            const listaCarrito = document.getElementById('listaCarrito');
            if (listaCarrito) {
                listaCarrito.innerHTML = '<p>Tu carrito está vacío.</p>';
            }




            const contador = document.getElementById('contadorCarrito');
            if (contador) {
                contador.textContent = '0';
            }

            // Desactivar botón
            document.getElementById('btnPagar').disabled = true;
        } else {
            alert('❌ Error al procesar el pago (respuesta incorrecta del servidor).');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('❌ Error al procesar el pago (fallo en la petición).');
    });
});




// Recargar o redirigir después del pago al hacer clic en "Aceptar"
document.addEventListener('DOMContentLoaded', function () {
  const btnAceptarPago = document.getElementById('btnAceptarPago');
  const modalPago = bootstrap.Modal.getOrCreateInstance(document.getElementById('modalPagoExitoso'));

  if (btnAceptarPago) {
    btnAceptarPago.addEventListener('click', function () {
      modalPago.hide();  // Cierra el modal manualmente

      // Pequeño delay para dejar que el modal se cierre visualmente
      setTimeout(() => {
        location.reload(); // O redirige: window.location.href = '/user';
      }, 300);
    });
  }
});

