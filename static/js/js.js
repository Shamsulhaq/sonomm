$(document).ready(function() {
    
     //========== Header Fixed
     $(window).scroll(function() {
        if($(window).scrollTop() > 660) {
               $('.header').addClass('fixTop');
        }
        else {
               $('.header').removeClass('fixTop');
        }
    });
    
    
        //============= Check all page sign    
    
        $('.checkAddress').on('click', function(){
            $('.checkAddress').removeClass('current');
            $(this).addClass('current');
        });
      

        //--------------- Edit by MBM

        $(".addBtmBtn").click(function(){
            $(".AddForm").show();
        })
        $(".removeAdForm").click(function(){
            $(".AddForm").hide();
        })
    
    
        
        $('.payBtn').on('click', function(){
            $('.payBtn').removeClass('activeBtn');
            $(this).addClass('activeBtn');
        });

    
    //========== Menu Btn
    
	$(".openCloseBtn").click(function(){
        $(".mainMenu").slideToggle();
    });
    
    //========== All Menu Btn
    
	$(".catgryMenu").click(function(){
        $(".catMenuIn").slideToggle();
    });
    

     //========== login Btn
    
	$(".login").click(function(){
        $(".loginBox").slideToggle();
    });
    
    //========== login Btn
    
	$(".cartImg").click(function(){
        $(".cartItemBox").slideToggle();
    });
    
        
     //========== fancybox
    
    $('[data-fancybox]').fancybox({
          protect: true,
          buttons : [
            'slideShow',
            'fullScreen',
            'thumbs',
            'share',
            'zoom',
            'close',              
        ]
    });
    
    //========== Top slider Slider
	$('.topSlider > ul').slick({
		arrows: true,
		dots: false,
		speed: 200,
		slidesToShow:1,
		slidesToScroll: 1,
		autoplay: true,
        fade:true,
		responsive: [
			{
				breakpoint: 640,
				settings: {
                    arrows: false,
                    dots: true,
				}
			}
		]
	});
    
    //========== Latest News Slider
        $('.latestNews ul').slick({
            arrows: false,
            dots: false,
            infinite: true,
            speed: 200,
            slidesToShow:1,
            slidesToScroll: 1,
            autoplay: true,
        });
    
    //========== Product Slider
	$('.prdctLeftBox > ul').slick({
		arrows: false,
		dots: true,        
		infinite: true,
		speed: 200,
		slidesToShow:1,
		slidesToScroll: 1,
		autoplay: true,
	});
    
    
    //========== Big Offer Slider
        $('.bigOfrSlid').slick({
            arrows: false,
            dots: true,        
            infinite: true,
            speed: 200,
            slidesToShow:1,
            slidesToScroll: 1,
            autoplay: true,
        });
    
    //========== Big Add Slider
        $('.bigAddBox .row').slick({
            arrows: true,
            dots: false,        
            infinite: true,
            speed: 200,
            slidesToShow:1,
            slidesToScroll: 1,
            autoplay: true,
        });
    
    
    //========== Brand logo Slider
        $('.brandIn').slick({
            arrows: false,
            dots: false,        
            infinite: true,
            speed: 200,
            slidesToShow:5,
            slidesToScroll: 1,
            autoplay: true,
            responsive: [
                {
                    breakpoint:640,
                    settings: {
                        slidesToShow:3,
                        dots: true,
                    }
                },
                {
                    breakpoint:480,
                    settings: {
                        slidesToShow:2,
                        dots: true,
                    }
                },
            ]
        });
    
    //========== Best Sellers Slider
        $('.teamSldr').slick({
            arrows: false,
            dots: false,        
            infinite: true,
            speed: 200,
            slidesToShow:4,
            slidesToScroll: 1,
            autoplay: false,
            responsive: [
                {
                    breakpoint:1023,
                    settings: {
                        slidesToShow:3,
                        dots: true,
                    }
                },
                {
                    breakpoint:767,
                    settings: {
                        slidesToShow:2,
                        dots: true,
                    }
                },
                {
                    breakpoint:639,
                    settings: {
                        slidesToShow:2,
                        dots: true,
                    }
                },
                {
                    breakpoint:439,
                    settings: {
                        slidesToShow:1,
                        dots: true,
                    }
                },
            ]
        });    
    
     //========== Remarks Slider
        $('ul.remarksSlider').slick({
            arrows: false,
            dots: true,        
            infinite: true,
            speed: 200,
            slidesToShow:1,
            slidesToScroll: 1,
            autoplay: true,
        });
    
    //========== Organic Slider
        $('.organicSlider > .row').slick({
            arrows: false,
            dots: true,        
            infinite: true,
            speed: 200,
            slidesToShow:4,
            slidesToScroll: 1,
            autoplay: false,
            responsive: [
                {
                    breakpoint:1023,
                    settings: {
                        slidesToShow:3,
                        dots: true,
                    }
                },
                {
                    breakpoint:767,
                    settings: {
                        slidesToShow:2,
                        dots: true,
                    }
                },
                {
                    breakpoint:639,
                    settings: {
                        slidesToShow:1,
                        dots: true,
                    }
                },
                {
                    breakpoint:439,
                    settings: {
                        slidesToShow:1,
                        dots: true,
                    }
                },
            ]
        });
    
    
    //========== BackTop
    
    $(window).scroll(function() {
        if($(window).scrollTop() > 200) {
            $('.back-top').addClass('backTop');
        }
        else {
            $('.back-top').removeClass('backTop');
        }
    });
    
	$('.back-top').click(function() {
        $('body,html').animate({
            scrollTop: 0
        }, 1200, 'swing');
        return false;
    });
    
    
    //========== portfolio fillter   
    
     $('.portList li').on('click', function(){
         
          $('.portList li').removeClass("active");
          $(this).addClass("active");
         
         
         var selector = $(this).attr("data-filter");         
          $('.projectList').isotope({
              filter:selector,
          });         
     })    
    $('.projectList').isotope();
    
    
    // =============== Initialize Smart Cart    	
    $('#smartcart').smartCart();
    
    
    //============= Product Quantity
    
    $('.add').click(function () {
		if ($(this).prev().val() < 10) {
    	$(this).prev().val(+$(this).prev().val() + 1);
		}
    });
    $('.sub').click(function () {
        if ($(this).next().val() > 1) {
        if ($(this).next().val() > 1) $(this).next().val(+$(this).next().val() - 1);
        }
    });
    

    
    
});

  //============= Registration Checkbox
    function show1(){
      document.getElementById('div1').style.display ='block';
    }
    function show2(){
      document.getElementById('div1').style.display = 'none';
    }
  //============= Account Information change password
    function ShowHideDiv(chkPassword) {
        var dvChngPass = document.getElementById("dvChngPass");
        dvChngPass.style.display = chkPassport.checked ? "block" : "none";
    }

