<script setup>
/* eslint-disable */
import tradeimg from '../assets/images/tradeimg.jpg'

// data
const data = {
    inlineStyle: {
        backgroundImage: `url(${tradeimg})`,
    }
}
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col gap-16 pb-10">

            <div class="w-full h-60 bg-cover bg-center bg-opacity-50 flex flex-col items-center justify-center gap-2 md:h-96" :style="data.inlineStyle">
                <h1 class="text-2xl text-white font-black md:text-6xl">Trade Top Cryptocurrencies</h1>
                <p class="w-9/12 text-center text-xs text-normal text-slate-200 md:text-base">Bitcoin, Ethereum, Ripple and other crypto assets at your disposal</p>
            </div>

            <div class="w-11/12 mx-auto flex flex-col gap-7 md:w-9/12">

                <div class="flex flex-col gap-3">
                    <h3 class="text-bold text-sm text-white md:text-lg">Build Your Cryptocurrency Trading Portfolio with LibExTrades</h3>
                    <p class="text-xs text-slate-400 font-normal md:text-sm">
                        LibExTrades is excited to announce the launch of our new cryptocurrency trading platform. Now you can start trading
                        Bitcoin, Ethereum and many more cryptocurrencies quickly, easily and safely from wherever you are — in just seconds.
                        You get great margin trading leverage and short sell options with fast deposits and withdrawals. Our support team is
                        available 24/7/365 to help get you trading on our CySEC-regulated platform with a trading volume of US $11 billion
                        monthly.
                    </p>
                </div>

                <div class="flex flex-col gap-3">
                    <h3 class="text-bold text-sm text-white md:text-lg">What is a crypto currency</h3>
                    <p class="text-xs text-slate-400 font-normal md:text-sm">
                        A cryptocurrency like bitcoin is a virtual currency traded peer-to-peer on a blockchain, independent of centralized
                        authorities like banks and governments. Cryptocurrencies are entirely virtual, so they are not backed by physical
                        commodities and have no intrinsic value.
                    </p>
                </div>

                <div class="flex flex-col gap-3">
                    <h3 class="text-bold text-sm text-white md:text-lg">How Do Cryptocurrencies Work?</h3>
                    <p class="text-xs text-slate-400 font-normal md:text-sm">
                        Primarily, cryptocurrencies rely on blockchain technology to complete a transaction via an intricate P2P network.
                        Once a transfer request is entered into the network, it is validated by the network and added to a pool of other
                        transactions to create a block of data for the ledger, which is then entered into the existing blockchain. Once
                        the block is successfully added to the chain, the transaction is approved and completed.
                    </p>
                </div>

                <div class="flex flex-col gap-3">
                    <h3 class="text-bold text-sm text-white md:text-lg">Are There Investment Opportunities with Cryptocurrencies?</h3>
                    <p class="text-xs text-slate-400 font-normal md:text-sm">
                        Absolutely. Cryptocurrencies have become established investment commodities among major financial institutions
                        and have even been adopted by countries such as Australia and Japan. As with any investment though, there are
                        risks linked to market movements, high volatility and economics.
                    </p>
                </div>

            </div>

        </div>

    </div>
</template>