using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace DeggCryptor
{
    class AesHelper
    {
        public static string Encrypt(string input, string password)
        {
            return Convert.ToBase64String(Encrypt(Encoding.UTF8.GetBytes(input), password));
        }
        public static byte[] Encrypt(byte[] input, string password)
        {
            PasswordDeriveBytes pdb = new PasswordDeriveBytes(password, new byte[] { 0x43, 0x87, 0x23, 0x72, 0x45, 0x56, 0x68, 0x14, 0x62, 0x84 });
            MemoryStream ms = new MemoryStream();
            Aes aes = new AesManaged();
            aes.Key = pdb.GetBytes(aes.KeySize / 8);
            aes.IV = pdb.GetBytes(aes.BlockSize / 8);
            CryptoStream cs = new CryptoStream(ms, aes.CreateEncryptor(), CryptoStreamMode.Write);
            cs.Write(input, 0, input.Length);
            cs.Close();
            return ms.ToArray();
        }
        public static string Decrypt(string input, string password)
        {
            return Encoding.UTF8.GetString(Decrypt(Convert.FromBase64String(input), password));
        }
        public static byte[] Decrypt(byte[] input, string password)
        {
            PasswordDeriveBytes pdb = new PasswordDeriveBytes(password, new byte[] { 0x43, 0x87, 0x23, 0x72, 0x45, 0x56, 0x68, 0x14, 0x62, 0x84 });
            MemoryStream ms = new MemoryStream();
            Aes aes = new AesManaged();
            aes.Key = pdb.GetBytes(aes.KeySize / 8);
            aes.IV = pdb.GetBytes(aes.BlockSize / 8);
            CryptoStream cs = new CryptoStream(ms, aes.CreateDecryptor(), CryptoStreamMode.Write);
            cs.Write(input, 0, input.Length);
            cs.Close();
            return ms.ToArray();
        }

    }
}
