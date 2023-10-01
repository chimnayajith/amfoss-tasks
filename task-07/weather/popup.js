const apiKey = "37f1eda6887b09ac4269e7c94113ef4f"; 
const cityName = document.getElementById("city-name");
const editIcon = document.getElementById("edit-icon");
const locationInput = document.getElementById("location-input");
const locationInputContainer = document.querySelector(".location-input");

// weather using default
function fetchWeatherByCoords(latitude, longitude) {
  const apiUrl = `http://api.weatherstack.com/current?access_key=${apiKey}&query=${latitude},${longitude}`;
  
  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      cityName.textContent = data.location.name;
      document.getElementById("temperature").textContent =
        data.current.temperature + "°C";
      document.getElementById("condition").textContent =
        data.current.weather_descriptions[0];
    })
    .catch((error) => {
      console.error("Error fetching weather data:", error);
    });
}

// weather search
function searchWeatherByCity(city) {
  const apiUrl = `http://api.weatherstack.com/current?access_key=${apiKey}&query=${city}`;

  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      cityName.textContent = data.location.name;
      document.getElementById("temperature").textContent =
        data.current.temperature;
      document.getElementById("condition").textContent =
        data.current.weather_descriptions[0];

      editIcon.src = "./assets/edit.svg";
    })
    .catch((error) => {
      console.error("Error fetching weather data:", error);
    });
}

// toggle edit and search icon 0_0
function toggleIcons() {
  if (editIcon.src.includes("edit.svg")) {
    const cityName = document.getElementById("city-name");
    cityName.innerHTML =
      '<input type="text" id="location-input" class="hidden" placeholder="Enter city">';
    editIcon.src = "./assets/search.svg";
    const locationInput = document.getElementById("location-input");
    locationInput.focus();
    cityName.classList.add("hidden");
  }
}

// click event listener to toggle edit and search icon
editIcon.addEventListener("click", toggleIcons);

document.getElementById("edit-icon").addEventListener("click", function () {
  const locationInput = document.getElementById("location-input");
  const city = locationInput.value.trim();
  if (city) {
    searchWeatherByCity(city);
    toggleIcons();
  }
});

// checking if geolocation permission is there
if ("geolocation" in navigator) {
  
  // get current coordinates
  navigator.geolocation.getCurrentPosition(
    function (position) {
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;

      // Fetch weather based on coordinates
      fetchWeatherByCoords(latitude, longitude);
    },
    function (error) {
      console.error("Error getting location:", error);
    }
  );
} else {
  console.error("Geolocation is not supported in this browser.");
}
