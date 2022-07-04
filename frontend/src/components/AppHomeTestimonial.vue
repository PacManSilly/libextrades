<script setup>
/* eslint-disable */
import man1 from '../assets/images/man1.jpg'
import man2 from '../assets/images/man2.jpg'
import man3 from '../assets/images/man3.jpg'
import woman1 from '../assets/images/woman1.jpeg'
import woman2 from '../assets/images/woman2.jpeg'
import woman3 from '../assets/images/woman3.jpeg'

const payouts = [
    {id: 1, name: "Novella Kujb", amount: "$15,587.00"},
    {id: 2, name: "Oswaldo Pfannerstill", amount: "$87,160.00"},
    {id: 3, name: "Kitty Grady", amount: "$88,128.00"},
    {id: 4, name: "Deonte Tromp", amount: "$15,587.00"},
    {id: 5, name: "Tate Runte", amount: "$25,587.00"},
    {id: 6, name: "Kadin Marquardt", amount: "$5,587.00"},
    {id: 7, name: "Einar Johnston", amount: "$34,587.00"},
    {id: 8, name: "Olin Wunsch", amount: "$45,587.00"},
    {id: 9, name: "Kasey Denesik", amount: "$51,587.00"},
    {id: 10, name: "Hollis Shields", amount: "$15,00.00"},
    {id: 11, name: "Mona Schmitt", amount: "$12,587.00"},
    {id: 12, name: "Kailey Abshire", amount: "$10,587.00"},
    {id: 13, name: "Aurelie Powlowski", amount: "$60,587.00"},
    {id: 14, name: "Pascale Wilkinson", amount: "$6,587.00"},
    {id: 15, name: "Ella Kullitan", amount: "$15,587.00"},
]

const testimonials = [
    {
        id: 1,
        name: "Oswaldo Pfannerstill",
        image: man1,
        detail: `The proper word to describe my feeling is Gratitude! Thank you very much Libextrades
            for sharing your successful strategy with us and give this opportunity to people. I believe
            your best achievement as an investment platform is that you have created a very powerful
            strategy, super successful,specially on daily charts that is simple to understand and apply.
            Congratulations! You deserve it all!`
    },
    {
        id: 2,
        name: "Tate Runte",
        image: woman1,
        detail: `I have been with Libextrades for quite a while on and off, and tried a few other things
            including US stock options trading and SPY options spreads with few friends during this time.
            I've come back to Libextrades solid approach as my focus, and find looking at daily trades, and
            strengths and weaknesses of the currency pairs is a good place to start each day as a trader.`
    },
    {
        id: 3,
        name: "Einar Johnston",
        image: man2,
        detail: `TAlso the levels shown on the MT4 chart template make great places to set targets regardless
            of what strategy I am using to enter. I wil recommend Libextrades anytime anyday.`
    },
    {
        id: 4,
        name: "Olin Wunsch",
        image: woman2,
        detail: `Very simple and secure method to make a bit of interest to your investments`
    },
    {
        id: 5,
        name: "Pascale Wilkinson",
        image: man3,
        detail: ` I no longer need to work. My investments with Libextrades Investment pays me daily. I was scared
            at first, but all my fears are gone now. A big "Thank You" to Libextrades Investment!`
    },
    {
        id: 6,
        name: "Ella Kullitan",
        image: woman3,
        detail: `I am extremely pleased with the Libextrades platform,in terms of ease and speed of use and reliability.`
    },
]

</script>

<template>
    <div class="w-full h-full min-h-full py-20">

        <div class="w-11/12 mx-auto flex flex-col gap-y-20 lg:w-10/12">

            <div class="flex flex-col items-center gap-2">
                <h2 class="text-white text-xl font-black md:text-3xl">Testimonials</h2>
                <p class="w-11/12 mx-auto text-center text-xs text-slate-500 md:text-sm lg:w-1/2">
                    See what our clients are saying
                </p>
            </div>

            <div class="w-full h-full flex flex-col items-center justify-center gap-y-10 lg:gap-5 lg:flex-row">

                <div class="order-2 w-full flex flex-col gap-10 bg-slate-800 rounded-md shadow-md shadow-slate-800 py-6 px-4 md:w-5/12 lg:order-1 lg:w-3/12">
                    <h3 class="text-slate-200 text-base text-center font-bold">Latest Payouts</h3>

                    <div class="w-full h-full flex flex-col gap-y-2">
                        <div v-for="pay in payouts" :key="pay.id" class="flex items-center justify-between text-slate-400 text-xs md:text-sm">
                            <span>{{pay.id}} {{pay.name}}</span>
                            <span>{{pay.amount}}</span>
                        </div>
                    </div>
                </div>

                <div class="order-1 w-full h-full grid grid-cols-2 gap-10 justify-between lg:order-2">
                    
                    <div v-for="user in testimonials" :key="user.id" class="flex flex-col items-center gap-2">
                        <div class="w-20 h-20 rounded-full overflow-hidden  md:w-32 md:h-32">
                            <img :src="user.image" class="w-full h-full object-cover object-center">
                        </div>
                        <div class="flex flex-col items-center gap-2">
                            <p class="text-slate-200 text-sm md:text-base">{{user.name}}</p>
                            <p class="text-slate-400 text-center text-xs md:text-sm">{{user.detail}}</p>
                        </div>
                    </div>

                </div>

            </div>

        </div>

    </div>
</template>