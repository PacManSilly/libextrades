<script setup>
/* eslint-disable */
import IconPhoneOutline from './icons/IconPhoneOutline.vue'
import IconMail from './icons/IconMail.vue'
</script>

<template>
    <div id="contactus" class="w-full h-full bg-slate-800 py-20">

        <div class="w-11/12 h-full mx-auto flex items-center lg:w-10/12">

            <div class="flex-1 flex flex-col gap-5">
                <h2 class="text-white text-2xl font-black md:4xl">Contact Us</h2>

                <span class="text-xs text-slate-400 md:text-sm">
                    701 Sheppard Ave W,<br>
                    North York, ON M3H 2S7, Canada. 
                </span>

                <div class="flex items-center gap-5">
                    <IconMail class="w-7 h-7 fill-slate-400" />
                    <span class="text-xs text-slate-400 md:text-sm">support@libextrades.com</span>
                </div>
            </div>

            <div class="flex-1 ">
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