title: Explore the city
layout: simple

<div class="swiper-buttons d-none d-sm-block">

<div class="swiper-button-prev"></div>

<div class="swiper-button-next"></div>

</div>

<div markdown="1" class="swiper">

<div markdown="1" class="col-12 swiper-wrapper">

<div markdown="1" class="swiper-slide">

![Coimbra 1](/static/images/coimbra/coimbra_01.jpg){:class='city-img'}

</div>

<div markdown="1" class="swiper-slide">

![Coimbra 2](/static/images/coimbra/coimbra_02.jpg){:class='city-img'}

</div>

<div markdown="1" class="swiper-slide">

![Coimbra 3](/static/images/coimbra/coimbra_03.jpg){:class='city-img'}

</div>

<div markdown="1" class="swiper-slide">

![Coimbra 4](/static/images/coimbra/coimbra_04.jpg){:class='city-img'}

</div>

<div markdown="1" class="swiper-slide">

![Coimbra 5](/static/images/coimbra/coimbra_05.jpg){:class='city-img'}

</div>

<div markdown="1" class="swiper-slide">

![Coimbra 6](/static/images/coimbra/coimbra_06.jpg){:class='city-img'}

</div>

<div markdown="1" class="swiper-slide">

![Coimbra 7](/static/images/coimbra/coimbra_07.jpg){:class='city-img'}

</div>

<div markdown="1" class="swiper-slide">

![Coimbra 8](/static/images/coimbra/coimbra_08.jpg){:class='city-img'}

</div>

</div>

Turismo do centro
{:class='swiper-description'}

</div>

<script>
  window.addEventListener("DOMContentLoaded", function(){
    const swiper = new Swiper('.swiper', {
      slidesPerView: "auto",
      grabCursor: true,
    loop: true,
      navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
  },
    });
  });
</script>
