<script setup>
/* eslint-disable */
import tradeimg from '../assets/images/tradeimg.jpg'
import IconUserCheck from './icons/IconUserCheck.vue';
import IconTransfer from './icons/IconTransfer.vue';
import IconLineChartUp from './icons/IconLineChartUp.vue';
import AppTopNav from './AppTopNav.vue';
import AppHomeContactUs from './AppHomeContactUs.vue';
import AppHomeFooter from './AppHomeFooter.vue';

// data
const data = {
    inlineStyle: {
        backgroundImage: `url(${tradeimg})`,
    }
}
</script>

<template>
    <div class="relative w-full h-full min-h-full">

        <nav class="fixed top-0 right-0 w-full">
            <AppTopNav />
        </nav>

        <div class="w-full h-full flex flex-col gap-16 pb-10">

            <div class="w-full h-60 bg-cover bg-center bg-opacity-50 flex flex-col items-center justify-center gap-2 md:h-96" :style="data.inlineStyle">
                <h1 class="text-2xl text-white font-black mt-16 md:text-6xl">Copy Expert Traders</h1>
                <p class="w-9/12 text-center  text-xs text-normal text-slate-200 md:text-base">You dont need to be an expert trader to make profit, just copy traders</p>
            </div>

            <div class="w-11/12 mx-auto flex flex-col gap-16 md:w-9/12">

                <div class="flex flex-col gap-3">
                    <p class="text-xs text-slate-400 font-normal md:text-sm">
                        LibExTrades Copy Trading is both a product and a service. We cater to both the traders and investors. Being able
                        to copy trades from several expert traders is a great service in and of itself.
                        <br><br>
                        We originally wanted to put together a portfolio and manage everyone’s funds in one account but we soon realized
                        that account segregation and being in control of your funds is the only way to go, especially if we wanted to bring
                        in outside investors. So, after looking around and finding out that there was no way for anyone to copy someone
                        else’s trades (unlike any other market), we decided to start working on this project.
                        <br><br>
                        There have been many challenges and obstacles to overcome but when something is worth pursuing you do it even if
                        it’s hard. While the service is still being refined and improved on the daily bases we are actively connecting
                        traders and investors for the mutual benefit in trading and investing.
                    </p>
                </div>

                <div class="flex flex-col gap-10">
                    <h3 class="text-bold font-black text-sm text-center text-white md:text-lg">How Copy Trading Works</h3>

                    <div class="grid grid-cols-1 gap-y-5 items-center justify-between md:grid-cols-2 lg:grid-cols-3">

                        <div class="flex flex-col items-center gap-3">
                            <p class="text-xs text-slate-400 font-normal md:text-sm">1. Register and Fund Your Account</p>
                            <IconUserCheck class="w-12 h-12 fill-slate-400 md:w-20 md:h-20" />
                        </div>

                        <div class="flex flex-col items-center gap-3">
                            <p class="text-xs text-slate-400 font-normal md:text-sm">2. Copy One or More Expert Traders</p>
                            <IconTransfer class="w-12 h-12 fill-slate-400 md:w-20 md:h-20" />
                        </div>

                        <div class="flex flex-col items-center gap-3">
                            <p class="text-xs text-slate-400 font-normal md:text-sm">3. Watch Your Profits Grow</p>
                            <IconLineChartUp class="w-12 h-12 fill-slate-400 md:w-20 md:h-20" />
                        </div>

                    </div>
                </div>

                <div class="flex flex-col gap-3">
                    <p class="text-xs text-slate-400 font-normal md:text-sm">
                        Here is how the copier works: You, as an investor, simply select an expert or experts that you want to copy trades
                        from. Once you are signed up, this is the only action needed on your part.
                        <br><br>
                        Once you’ve taken care of the above, you are all set. There are no codes that you need to run or signals for you
                        to manually input. Our software will handle the trade copying automatically on your behalf. We monitor your experts
                        trading activity and as soon as there is a trade, we calculate all the necessary parameters and execute the trade.
                        <br><br>
                        The only thing you have to make sure of is that you have enough funds available in your trading account. When the
                        expert exits a position, you too will exit it. Automatically.
                    </p>
                </div>

            </div>

        </div>

        <AppHomeContactUs />
        <AppHomeFooter />

    </div>
</template>