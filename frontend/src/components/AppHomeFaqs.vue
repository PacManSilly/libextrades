<script setup>
/* eslint-disable */
import IconPlusCircle from './icons/IconPlusCircle.vue'
import IconMinusCircle from './icons/IconMinusCircle.vue'
import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
import { onMounted, ref, reactive } from 'vue';
gsap.registerPlugin(ScrollTrigger);

// resf
const faqs = ref("")
const faqsHead = ref("")
const faqsCard = ref("")


// data
const faqId = ref(null)
const obj = reactive({
    faqs: [
        {id: 1, state: false, q: "Why should i use your services", a: "We are a trusted and verified crypto investment platform with over 8 years of experience"},
        {id: 2, state: false, q: "Can i trust your services", a: "With over twenty thousand trades and 99.9% customer satisfaction, you without a doubt can trust our services"},
        {id: 3, state: false, q: "Do you have the best ROI", a: 'We have the highest "Return on Investment" in the industry'},
        {id: 4, state: false, q: "How fast do i get my withdrawals", a: "You get your profits as soon as you make the withdrawal request. Immediate payment is assured"},
        {id: 5, state: false, q: "Is my data with you save", a: "We do not in any way share your data with others. And your trade with us is safe and secure."},
        {id: 6, state: false, q: "What are your payment methods", a: "We accept bitcoin payment only"},
        {id: 7, state: false, q: "Is my trade with you secure", a: "100% safe, secure and reliable"},
        {id: 8, state: false, q: "Can i keep in touch with you", a: "Our customer care line and social media accounts are always active 24/7"},
    ]
})

// methods
const activateFaq = (id) => {
    obj.faqs.forEach((faq) => {
        if (faq.id == id) faq.state = !faq.state;
        else faq.state = false;
    });
}

// methods
const animFaqs = () => {
   gsap.from(faqsHead.value, {scrollTrigger: {trigger: faqs.value, start: "200px bottom", markers: false, id: "faqs"}, duration: 1, y: 100, opacity: 0})
   gsap.from(faqsCard.value, {scrollTrigger: {trigger: faqs.value, start: "500px bottom", markers: false, id: "faqs"}, duration: 1, y: 100, opacity: 0, stagger: 0.2})
}

// hooks
onMounted(() => {
    animFaqs()
})
</script>

<template>
    <div id="faqs" ref="faqs" class="w-full h-full min-h-full py-20 bg-white">

        <div class="w-11/12 mx-auto flex flex-col gap-y-10 lg:gap-y-20 lg:w-10/12">

            <div ref="faqsHead" class="flex flex-col items-center gap-2">
                <h2 class="text-slate-900 text-xl font-black md:text-3xl">Frequently Asked Questions</h2>
                <p class="w-11/12 mx-auto text-center text-xs text-slate-600 md:text-sm lg:w-1/2">
                    Can’t find the answers you are looking for? <RouterLink to="#contactus" class="text-blue-500">Contact us.</RouterLink>
                </p>
            </div>

            <!-- start of faqs -->
            <div class="w-full grid grid-cols-1 gap-2 py-4 mx-auto md:grid-cols-2 lg:w-9/12 lg:gap-10">
                <transition-group name="smooth">
                
                    <span ref="faqsCard" v-for="faq in obj.faqs" :key="faq.id" :class="faq.state ?'bg-slate-100':'bg-transparent'" class="group faqs flex flex-col space-y-3 p-4 rounded hover:bg-blueGray-100">

                        <!-- start of faq button -->
                        <button @click.prevent="activateFaq(faq.id)" class="flex items-center space-x-3">
                            <!-- start of icon -->
                            <IconMinusCircle  v-if="faq.state" class="w-5 h-5 fill-current text-amber-500" />
                            <IconPlusCircle v-else class="w-5 h-5 fill-current text-blueGray-700 group-hover:text-amber-500" />
                            <!-- end of icon -->
                            
                            <span class="text-sm text-blueGray-700 md:text-base">{{faq.q}}?</span>
                        </button>
                        <!-- end of faq button -->

                        <!-- start of faq answer -->
                        <transition
                            name="slide-down"
                            enter-from-class="-translate-y-1"
                            enter-active-class="transition duration-100"
                            leave-to-class="-translate-y-3"
                            leave-active-class="transition duration-100">
                            <p v-if="faq.state" class="text-sm pl-8 text-blueGray-500">{{faq.a}}.</p>
                        </transition>
                        <!-- end of faq answer -->

                    </span>
                </transition-group>
            </div>
            <!-- end of faqs -->

        </div>

    </div>
</template>

<style>
    .smooth-move,
    .smooth-enter-active,
    .smooth-leave-active {
        @apply transition duration-300;
    }
</style>