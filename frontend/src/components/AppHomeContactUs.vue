<script setup>
/* eslint-disable */
import IconPhoneOutline from './icons/IconPhoneOutline.vue'
import IconMail from './icons/IconMail.vue'
import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
import { onMounted, ref } from 'vue';
gsap.registerPlugin(ScrollTrigger);

// refs
const contactus = ref("")
const contact1 = ref("")
const contact2 = ref("")

// methods
const animContactUs = () => {
    gsap.from([contact1.value, contact2.value], {scrollTrigger: {trigger: contactus.value, start: "200px bottom", markers: false, id: "contactus"}, duration: 1, y: 50, opacity: 0, stagger: 0.2})
}

// hooks
onMounted(() => {
    animContactUs()
})
</script>

<template>
    <div id="contactus" ref="contactus" class="w-full h-full bg-slate-800 py-20">

        <div class="w-11/12 h-full mx-auto flex flex-col gap-y-10 md:flex-row md:items-center lg:w-10/12">

            <div ref="contact1" class="flex-1 flex flex-col gap-5">
                <h2 class="text-white text-2xl font-black md:4xl">Contact Us</h2>

                <span class="text-xs text-slate-400 md:text-sm">
                    701 Sheppard Ave W,<br>
                    North York, ON M3H 2S7, Canada. 
                </span>

                <div class="flex items-center gap-3 md:gap-5">
                    <IconMail class="w-5 h-5 fill-slate-400 md:w-7 md:h-7" />
                    <a href="mailto:support@libextrades.com" class="text-xs text-slate-400 md:text-sm">support@libextrades.com</a>
                </div>
            </div>

            <div ref="contact2" class="flex-1 ">
                <p class="text-xs text-slate-400 font-normal md:text-sm">
                    The Transactions offered by this Website can be executed only by fully competent adults. Transactions with financial
                    instruments offered on the Website involve substantial risk and trading may be very risky. If you make Transactions
                    with the financial instruments offered on this Website, you might incur substantial losses or even lose everything in
                    your Account. Before you decide to start Transactions with the financial instruments offered on the Website, you must
                    review the Service Agreement and Risk Disclosure Information.
                </p>
            </div>

        </div>

    </div>
</template>